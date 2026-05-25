# 운정2동 2026 지방선거 OpenCrab 보강 데이터

Generated at: 2026-05-25T22:54:15.400Z

This supplement corrects interpretation of the existing NEC 2026 local election OpenCrab pack for 운정2동.

## Files

- `unjeong2_guide.md`: readable summary for OpenCrab ingest.
- `unjeong2_candidates.csv`: candidate and party-list metadata with document availability.
- `unjeong2_document_status.jsonl`: one JSON record per candidate or party document-status row.
- `graph/nodes.jsonl`: typed guide, contest, candidate, party, document, and document-status nodes.
- `graph/edges.jsonl`: typed relationships connecting guide, contests, candidates, parties, documents, and document statuses.
- `verification_summary.json`: local verification counts and interpretation.

## Important Interpretation

The 9 available five-pledge documents are already in the OpenCrab package. The local 운정2동 constituency and proportional records are metadata-only because the official NEC policy API returned no downloadable PDF path for those entries at verification time.
