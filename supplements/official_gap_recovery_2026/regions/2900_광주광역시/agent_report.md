# Agent Report: 2900 광주광역시

Checked at: 2026-05-26T09:09:58.6656170+09:00

## Scope

- Read: 	argets.csv only.
- Wrote: official_hits.jsonl, gent_report.md.
- Accepted source class: official NEC institutional source, policy.nec.go.kr.
- Rejected source class: party, candidate, news, private, and generic guidance pages. No generic guidance page was counted as a hit.

## Method

For each target row, I queried the official Policy Pledge site structured endpoint with the exact election, province, district, and election type parameters, then matched the returned official record by candidate/party, party name, district, and target document type.

Official endpoint used: POST https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do

## Counts

- Targets checked: 42
- Candidate-specific official structured records: 41
- Party-specific official structured records: 1
- Official structured records matched: 42
- Recoverable target document files found: 0
- Matched official records with no target document file path: 42
- Official records not found: 0
- Matched records with ileDispYn=Y: 9
- Matched records with ileDispYn=N: 33
- Official guidance-only hits accepted: 0
- Non-official hits accepted: 0

## Result

No target document had a non-empty official file path in the exact matching official structured record at check time. Several neighboring non-target document slots in the same candidate records had file paths, but those were not accepted because they did not match the target document type.

official_hits.jsonl contains one JSON object per target, including the official API query, exact searched terms, match status, raw ileinfo entry, and document_found=false for all rows.