# 서울특별시 official gap recovery report

- Work unit: `1100_서울특별시`
- Target file read: `targets.csv`
- Official sources used: `policy.nec.go.kr` candidate/party pledge page and `policy.nec.go.kr/plc/commiment/initUCACommimentList.do`
- Search date: 2026-05-26 KST

## Method

Each target was checked against the official NEC structured endpoint using exact target scope:

- Candidate rows: matched `huboid`, candidate name, party, district, and target document type.
- Party rows: matched party, district, proportional election type, and official party submission record.
- Accepted only non-empty official target-document file paths from official NEC records.
- Rejected non-target official documents, including available `5대공약` PDFs when the target type was `선거공약서`.
- Rejected non-official/private/search-result sources.

## Counts

- Targets checked: 237
- Official endpoint requests: 101
- Exact official records found: 237
- Accepted official hits: 0
- Exact official records with no target document file path or unpublished file status: 237
- Missing exact official records: 0
- Official guidance-only sources accepted as hits: 0

## Result

No target-specific recoverable official policy document was found for the 서울특별시 target set under the strict matching rule. The official NEC records exist for all targets, but the exact target document fields remain empty or unpublished for these rows.

`official_hits.jsonl` was written with 0 hit records.
