# Official gap recovery report: 강원특별자치도

## Scope
- Target file read: `targets.csv`
- Official sources used: `policy.nec.go.kr` candidate promise page and its official structured JSON endpoints.
- Rejected sources: party, candidate, news, private, and generic guidance pages.

## Method
Queried the official 제9회 전국동시지방선거 후보자공약 structured endpoint by election unit and district, then accepted only records matching exact candidate `huboid` or party name plus district plus requested document type. Generic submission guidance was not counted as a hit.

## Counts
- Targets searched: 80
- Unique official district queries: 39
- Official structured-record hits written: 80
- Downloadable target PDFs found: 0
- Official structured records with no target PDF path/open download: 80
- No matching official record: 0
- Candidate records where requested doc type was not listed: 0
- Official guidance-only accepted: 0

## Counts by requested document type
- 비례대표 정당 제출자료: 8
- 선거공보: 25
- 선거공약서: 47

## Counts by recovery status
- official_structured_record_no_target_file: 80

## Output files
- `official_hits.jsonl`
- `agent_report.md`
