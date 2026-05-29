from __future__ import annotations

import csv
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parents[3]
MANIFEST_PATH = BASE_DIR / "newly_available_document_manifest.csv"
MARKDOWN_DIR = BASE_DIR / "direct_nec_downloads" / "markdown"
OUT_DIR = BASE_DIR / "corrected_candidate_only_cloud_pack"
ZIP_PATH = BASE_DIR / "opencrab_nec_recheck_candidate_only_corrected_cloud_pack.zip"
VALID_MANIFEST_PATH = BASE_DIR / "valid_candidate_only_document_manifest.csv"
EXCLUDED_MANIFEST_PATH = BASE_DIR / "excluded_party_document_mismatch.csv"
SUMMARY_PATH = BASE_DIR / "corrected_pack_summary.json"


def stable_id(*parts: str, prefix: str = "") -> str:
    raw = "|".join(str(part) for part in parts)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
    return f"{prefix}{digest}" if prefix else digest


def read_rows() -> list[dict[str, str]]:
    with MANIFEST_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def parse_int(value: str) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except ValueError:
        return None


def read_markdown(row: dict[str, str]) -> str:
    rel_path = row["local_markdown_repo_path"].replace("/", "\\")
    md_path = REPO_ROOT / rel_path
    if not md_path.exists():
        md_path = MARKDOWN_DIR / Path(row["local_markdown_repo_path"]).name
    return md_path.read_text(encoding="utf-8")


def chunk_text(text: str, max_chars: int = 4500, overlap: int = 350) -> list[str]:
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + max_chars)
        if end < len(text):
            split_at = max(text.rfind("\n## ", start, end), text.rfind("\n\n", start, end))
            if split_at > start + max_chars // 2:
                end = split_at
        chunks.append(text[start:end].strip())
        if end >= len(text):
            break
        start = max(0, end - overlap)
    return [chunk for chunk in chunks if chunk]


def put_node(nodes: dict[str, dict], node_id: str, node_type: str, label: str, properties: dict) -> None:
    if node_id in nodes:
        nodes[node_id]["properties"].update({k: v for k, v in properties.items() if v not in (None, "")})
        return
    nodes[node_id] = {
        "id": node_id,
        "type": node_type,
        "label": label,
        "properties": {k: v for k, v in properties.items() if v not in (None, "")},
    }


def put_edge(edges: set[tuple[str, str, str]], source: str, target: str, relation: str) -> None:
    edges.add((source, target, relation))


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for record in records:
            # Keep JSONL physically one record per line even when PDF text contains
            # Unicode line separators that Python's splitlines() would treat as breaks.
            f.write(json.dumps(record, ensure_ascii=True, separators=(",", ":")) + "\n")


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def clean_for_filename(text: str) -> str:
    text = re.sub(r"[^\w가-힣.-]+", "_", text, flags=re.UNICODE)
    return text.strip("_")[:120]


def main() -> None:
    rows = read_rows()
    valid_rows = [row for row in rows if row["doc_type"] != "비례대표 정당 제출자료"]
    excluded_rows = []
    for row in rows:
        if row["doc_type"] == "비례대표 정당 제출자료":
            fixed = dict(row)
            fixed["exclusion_reason"] = (
                "excluded_from_corrected_pack: current NEC path does not carry enough province identity "
                "for safe recovery matching, and the earlier batch reused one party-doc markdown/pdf filename"
            )
            excluded_rows.append(fixed)

    if len(valid_rows) != 132:
        raise RuntimeError(f"Expected 132 valid candidate rows, got {len(valid_rows)}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for subdir in ("cloud", "graph"):
        (OUT_DIR / subdir).mkdir(parents=True, exist_ok=True)

    created_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    root_id = "supplement:official-gap-recovery-recheck-2026-05-29-candidate-only-corrected"
    source_id = "source:policy-nec-go-kr"

    nodes: dict[str, dict] = {}
    edges: set[tuple[str, str, str]] = set()
    documents: list[dict] = []
    chunks: list[dict] = []

    put_node(
        nodes,
        root_id,
        "OfficialGapRecoveryRecheck",
        "2026 지방선거 중앙선관위 재확인 보강 후보자 문서 보정본",
        {
            "generated_at": created_at,
            "source_site": "https://policy.nec.go.kr",
            "valid_candidate_documents": len(valid_rows),
            "excluded_party_documents": len(excluded_rows),
            "original_recheck_documents": len(rows),
            "correction_reason": "Excluded party-list documents because district/party-only matching caused cross-province mismatches.",
        },
    )
    put_node(
        nodes,
        source_id,
        "OfficialSource",
        "중앙선관위 정책·공약마당",
        {"url": "https://policy.nec.go.kr", "reviewed_at": "2026-05-29"},
    )
    put_edge(edges, root_id, source_id, "RECHECKED_OFFICIAL_SOURCE")

    for row in valid_rows:
        text = read_markdown(row)
        row_hash = stable_id(row["record_id"], row["source_id"])
        doc_external_id = f"nec_recheck_candidate_doc_{row_hash}"
        title = f"{row['subSgName']} {row['sggname']} {row['hbjname'] or row['jdname']} {row['doc_type']}".strip()
        repo_path = row["local_markdown_repo_path"]
        source_url = f"https://raw.githubusercontent.com/treylom/opencrab-nec-2026-local-election-data/main/{repo_path}"
        sha256 = hashlib.sha256(text.encode("utf-8")).hexdigest()

        metadata = {
            "source_id": row["source_id"],
            "record_id": row["record_id"],
            "source_site": "https://policy.nec.go.kr",
            "province_id": row["province_id"],
            "province_name": row["province_name"],
            "subSgId": row["subSgId"],
            "subSgName": row["subSgName"],
            "sggname": row["sggname"],
            "huboid": row["huboid"],
            "candidate_or_party": row["hbjname"] or row["jdname"],
            "candidate_name": row["hbjname"],
            "party_name": row["jdname"],
            "doc_type": row["doc_type"],
            "download_url": row["new_current_download_url"],
            "official_pdf_path": row["new_current_pdf_path"],
            "extraction_method": row["extraction_method"],
            "quality_flag": row["quality_flag"],
            "pages": parse_int(row["pages"]),
            "chars": parse_int(row["chars"]),
            "bytes": parse_int(row["bytes"]),
            "recovery_batch": "official_gap_recovery_recheck_2026-05-29-candidate-only-corrected",
            "excluded_party_documents_from_prior_batch": len(excluded_rows),
        }

        documents.append(
            {
                "id": doc_external_id,
                "title": title,
                "source_type": "github",
                "source_url": source_url,
                "path": repo_path,
                "mime_type": "text/markdown",
                "bytes": len(text.encode("utf-8")),
                "sha256": sha256,
                "metadata": {k: v for k, v in metadata.items() if v not in (None, "")},
            }
        )

        for idx, chunk in enumerate(chunk_text(text), start=1):
            chunks.append(
                {
                    "id": f"{doc_external_id}_chunk_{idx:03d}",
                    "document_id": doc_external_id,
                    "ordinal": idx,
                    "text": chunk,
                    "metadata": {
                        "source_id": row["source_id"],
                        "record_id": row["record_id"],
                        "province_name": row["province_name"],
                        "sggname": row["sggname"],
                        "candidate_or_party": row["hbjname"] or row["jdname"],
                        "doc_type": row["doc_type"],
                        "quality_flag": row["quality_flag"],
                        "recovery_batch": "official_gap_recovery_recheck_2026-05-29-candidate-only-corrected",
                    },
                }
            )

        province_node = f"province:{row['province_id']}:{stable_id(row['province_id'], row['province_name'])}"
        contest_node = f"contest:{row['subSgId']}:{stable_id(row['province_id'], row['subSgId'], row['sggname'])}"
        party_node = f"party:{stable_id(row['jdname'])}" if row["jdname"] else ""
        candidate_node = f"candidate:{row['huboid']}" if row["huboid"] else ""
        doc_node = f"document:{row['source_id']}"

        put_node(nodes, province_node, "Province", row["province_name"], {"province_id": row["province_id"], "province_name": row["province_name"]})
        put_node(
            nodes,
            contest_node,
            "ContestRegion",
            f"{row['subSgName']} {row['sggname']}",
            {"subSgId": row["subSgId"], "subSgName": row["subSgName"], "sggname": row["sggname"], "province_name": row["province_name"]},
        )
        if party_node:
            put_node(nodes, party_node, "Party", row["jdname"], {"party_name": row["jdname"]})
        if candidate_node:
            put_node(
                nodes,
                candidate_node,
                "Candidate",
                row["hbjname"],
                {"huboid": row["huboid"], "candidate_name": row["hbjname"], "party_name": row["jdname"]},
            )
        put_node(
            nodes,
            doc_node,
            "NewlyAvailableOfficialDocument",
            title,
            {
                "source_id": row["source_id"],
                "record_id": row["record_id"],
                "doc_type": row["doc_type"],
                "official_download_url": row["new_current_download_url"],
                "official_pdf_path": row["new_current_pdf_path"],
                "markdown_repo_path": repo_path,
                "github_url": row["github_url"],
                "extract_status": row["extract_status"],
                "extraction_method": row["extraction_method"],
                "quality_flag": row["quality_flag"],
                "pages": parse_int(row["pages"]),
                "chars": parse_int(row["chars"]),
                "bytes": parse_int(row["bytes"]),
                "recheck_date": "2026-05-29",
                "recovery_class": row["recovery_class"],
            },
        )

        put_edge(edges, root_id, province_node, "HAS_NEWLY_AVAILABLE_PROVINCE_DOCUMENT")
        put_edge(edges, province_node, contest_node, "CONTAINS_CONTEST_REGION")
        if party_node:
            put_edge(edges, contest_node, party_node, "CONTEST_HAS_PARTY")
            put_edge(edges, doc_node, party_node, "DOCUMENT_PARTY")
        if candidate_node:
            put_edge(edges, candidate_node, contest_node, "RUNS_IN_CONTEST_REGION")
            put_edge(edges, doc_node, candidate_node, "DOCUMENT_FOR_CANDIDATE")
            if party_node:
                put_edge(edges, candidate_node, party_node, "AFFILIATED_WITH_PARTY")
        put_edge(edges, root_id, doc_node, "HAS_NEWLY_AVAILABLE_DOCUMENT")
        put_edge(edges, doc_node, source_id, "RECOVERED_FROM_OFFICIAL_SOURCE")
        put_edge(edges, doc_node, province_node, "DOCUMENT_PROVINCE")
        put_edge(edges, doc_node, contest_node, "DOCUMENT_CONTEST_REGION")

    edge_records = [{"source": s, "target": t, "relation": r, "properties": {}} for s, t, r in sorted(edges)]
    node_records = list(nodes.values())

    manifest = {
        "format": "opencrab-cloud-pack-v1",
        "title": "nec-2026-local-election-newly-available-official-candidate-documents-corrected",
        "version": "2026-05-29.2",
        "created_at": created_at,
        "source": "https://policy.nec.go.kr/",
        "repository": "https://github.com/treylom/opencrab-nec-2026-local-election-data",
        "counts": {
            "documents": len(documents),
            "chunks": len(chunks),
            "nodes": len(node_records),
            "edges": len(edge_records),
        },
        "notes": (
            "Corrected supplement containing 132 candidate/election-office documents. "
            "Fourteen party-list documents from the previous 146-document batch were excluded "
            "because cross-province matching and filename collisions made them unsafe."
        ),
    }

    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_jsonl(OUT_DIR / "cloud" / "documents.jsonl", documents)
    write_jsonl(OUT_DIR / "cloud" / "chunks.jsonl", chunks)
    write_jsonl(OUT_DIR / "graph" / "nodes.jsonl", node_records)
    write_jsonl(OUT_DIR / "graph" / "edges.jsonl", edge_records)

    write_csv(VALID_MANIFEST_PATH, valid_rows, list(rows[0].keys()))
    write_csv(EXCLUDED_MANIFEST_PATH, excluded_rows, list(rows[0].keys()) + ["exclusion_reason"])

    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for rel in [
            "manifest.json",
            "cloud/documents.jsonl",
            "cloud/chunks.jsonl",
            "graph/nodes.jsonl",
            "graph/edges.jsonl",
        ]:
            zf.write(OUT_DIR / rel, rel)

    summary = {
        "generated_at": created_at,
        "valid_candidate_documents": len(valid_rows),
        "excluded_party_documents": len(excluded_rows),
        "cloud_pack_documents": len(documents),
        "cloud_pack_chunks": len(chunks),
        "graph_nodes": len(node_records),
        "graph_edges": len(edge_records),
        "zip_path": str(ZIP_PATH),
        "zip_bytes": ZIP_PATH.stat().st_size,
        "zip_sha256": hashlib.sha256(ZIP_PATH.read_bytes()).hexdigest(),
        "excluded_manifest": str(EXCLUDED_MANIFEST_PATH),
    }
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    sha_path = ZIP_PATH.with_suffix(ZIP_PATH.suffix + ".sha256")
    sha_path.write_text(f"{summary['zip_sha256']}  {ZIP_PATH.name}\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
