# 2026 NEC Official Gap Recovery

Generated at: 2026-05-25T23:58:45.066Z

This supplement targets official-source recovery for records that still have no downloadable PDF in the current NEC policy API.

Important correction: proportional election PDFs can be exposed through `filePathName + updtFileName`; this inventory treats those as currently available.

- official_gap_targets.csv: current official NEC API has no PDF path after this correction.
- pack_stale_direct_recovery_targets.csv: current NEC API has a PDF path, but the previous pack did not.
- regions/: one independent workload directory per province.

## Recovery result

- `pack_stale_currently_available`: 596 PDFs were downloaded again from `policy.nec.go.kr`.
- Markdown extraction succeeded for 595 files; 1 file has empty embedded text.
- The remaining 1,645 targets have official NEC structured records but no public PDF path.
- External official sources checked by province produced 0 additional candidate/party-specific downloadable documents.
- No unofficial source was accepted.

## OpenCrab-ready files

- `official_gap_recovery_summary.md`: human-readable investigation summary.
- `recovered_document_manifest.csv`: 596 directly recovered documents and Markdown paths.
- `current_missing_after_official_search.csv`: 1,645 unresolved official targets.
- `region_recovery_summary.csv`: province-level search summary.
- `merged_official_hits.jsonl`: province agent evidence records.
- `graph/nodes.jsonl` and `graph/edges.jsonl`: graph pack ontology.
- `direct_nec_downloads/markdown/*.md`: recovered PDF text.
- `direct_nec_downloads/quality_report.md`: extraction and visual sample check.

Local ZIP artifacts are intentionally ignored by git:

- `opencrab_official_gap_recovery_graph_pack.zip`
- `opencrab_official_gap_recovery_markdown_part_01.zip`
- `opencrab_official_gap_recovery_markdown_part_02.zip`
