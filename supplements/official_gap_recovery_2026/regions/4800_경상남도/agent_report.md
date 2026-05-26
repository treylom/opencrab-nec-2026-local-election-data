# 경상남도 official gap recovery report

## Scope
- Target file: `targets.csv`
- Region/work unit: 경상남도 (`4800`)
- Targets reviewed: 100
- Official sources allowed and used: `policy.nec.go.kr`, `data.go.kr`
- Output files written: `agent_report.md`, `official_hits.jsonl`

## Method
- Parsed only `targets.csv` for stable identifiers: `source_id`, `subSgId`, `sgTypecode`, `sggid`, `huboid`, `jdid`, and `doc_index`.
- Queried the official NEC policy page endpoint for 제9회 전국동시지방선거 후보자공약:
  - `https://policy.nec.go.kr/plc/commiment/initUCACommiment.do?menuId=CNDDT25`
  - `https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do`
- Matched candidate targets by official `huboid` and party proportional targets by official district name + `jdid`.
- Required exact target document type matching:
  - candidate `doc_index=1`: `선거공보`
  - candidate `doc_index=2`: `선거공약서`
  - party target: `비례대표 정당 제출자료` / official `선거공보` row
- Rejected generic guidance and adjacent document types. In particular, `5대공약` records were not accepted for `선거공약서` targets.

## Results
- Accepted official document hits: 0
- Candidate targets checked: 82
  - `선거공약서`: 54
  - `선거공보`: 28
- Party proportional targets checked: 18
- Distinct official NEC list queries: 41
- All 100 targets had candidate/party-specific official rows, but the requested target document entries had no official file path or target-type OCR/content record available.

## Rejection Summary
- 82 candidate records: target document type existed in the official structured row, but the target file path was empty.
- 18 party proportional records: official row existed, but `fileDispYn=N` and no file path was present.
- No party, candidate, news, private, or non-institutional sources were used.

## Output
- `official_hits.jsonl` is intentionally empty because no accepted hits were found.