# Official Gap Recovery Report - ?????

- Run timestamp: 2026-05-26 09:11:31 +0900
- Target file read: `targets.csv`
- Output files written: `agent_report.md`, `official_hits.jsonl`
- Allowed-source rule applied: accepted only `policy.nec.go.kr`, `data.go.kr`/`data.nec.go.kr`, `*.nec.go.kr`, and `*.go.kr`; party, candidate, news, and private sources were excluded.

## Search Method

- Queried the official NEC Policy Pledge candidate endpoint at `https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do`.
- Exact matching used `sgId=20260603`, target `subSgId`, `sgTypecode`, `province_id=2700`, target district/`sggid` where applicable, and then candidate `huboid` or party `jdname` plus `sggname`.
- For each matched official row, the requested `doc_type` was parsed from the official `fileinfo` structure. A record was emitted to `official_hits.jsonl` only when the requested target document had a non-empty official file path or download path.
- Generic NEC submission forms/guidance pages found on official regional NEC sites were treated as `official_guidance_only` and were not emitted as hits.

## Counts

- Total targets: 52
- Candidate-document targets: 37
- Party-document targets: 15
- Exact official structured records matched: 52
- Recovered official document hits with file path: 0
- Exact official records still showing no file path: 52
- No exact official record found: 0
- `official_hits.jsonl` records: 0

## No-Hit Breakdown

- 비례대표 정당 제출자료: 15 exact official records matched, but the requested document path was empty.
- 선거공보: 12 exact official records matched, but the requested document path was empty.
- 선거공약서: 25 exact official records matched, but the requested document path was empty.

## Conclusion

No recoverable official candidate/party-specific document URL was found for the target set. The official policy endpoint still returns target-specific records for all 52 rows, but the requested missing document slots remain empty (`page_count`/file count `0`, blank file path, or party `0||` placeholder), so no JSONL hit was emitted.
