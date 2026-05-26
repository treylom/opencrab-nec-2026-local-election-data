# Official Gap Recovery Report - 충청북도 (4300)

## Scope
- Target file: targets.csv
- Region/work unit: 충청북도
- Election: 제9회 전국동시지방선거
- Official sources used: policy.nec.go.kr only
- Rejected sources: party, candidate, news, private, and generic guidance pages were not used as hits.

## Method
- Queried the official NEC candidate pledge endpoint: https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do
- Matched candidate targets by huboid, candidate name, district, party, and requested document type.
- Matched party target by party id/name, district, and official submitted-material record.
- Counted a PDF document hit only when the official structured record exposed a non-empty PDF path for the requested document type.
- Counted an official structured record hit when the exact candidate/party-specific official record existed but the requested document's PDF path was empty.

## Counts
- Targets reviewed: 45
- official_hits.jsonl records: 45
- Official PDF document hits recovered: 0
- Official structured-record-only hits: 45
- Candidate/party records without requested document entry: 0
- Not found in official structured records: 0
- official_guidance_only rejected: 0
- Unique official endpoint queries: 24

## Finding
All 45 targets matched official candidate- or party-specific NEC structured records, but every requested missing document type had an empty PDF path in the official record. No downloadable official PDF was recovered for the requested missing documents.

## Changed Files
- official_hits.jsonl
- agent_report.md