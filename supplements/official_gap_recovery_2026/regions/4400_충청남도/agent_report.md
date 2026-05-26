# Official Gap Recovery Report - 충청남도

Generated: 2026-05-26 09:25:27 +09:00

## Scope
- Input read: targets.csv in this directory only.
- Outputs written: official_hits.jsonl, agent_report.md.
- Official sources used: policy.nec.go.kr candidate/party commitment list JSON and cdn.nec.go.kr PDF HEAD checks.
- Rejected source classes: party, candidate, news, private, and generic guidance pages. No generic guidance-only records were counted as hits.

## Counts
- Targets reviewed: 61
- Accepted official records: 61
- Candidate records: 57
- Party records: 4
- Document URLs verified: 0
- Structured official records without available PDF: 61
- Misses: 0

## By Document Type
- 5대공약: 1 accepted (0 document, 1 structured-only)
- 선거공보: 19 accepted (0 document, 19 structured-only)
- 선거공약서: 41 accepted (0 document, 41 structured-only)

## Verified Document URLs
- none

## Misses
- none

## Notes
- A structured-only hit means the official NEC JSON matched the exact candidate/party, district, and document type, but the requested PDF path was blank or not published in the official record.
- For many chief executive and education superintendent targets, NEC lists a candidate-specific 선거공약서 entry with no PDF path while separate 5대공약 PDFs exist; only the requested document type was counted for each row.
- Proportional party rows are candidate/party-specific official structured records from policy.nec.go.kr; their official fileinfo value is 0|| and no PDF URL is currently available.
