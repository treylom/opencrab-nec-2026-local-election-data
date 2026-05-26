# Official-source recovery report - 대전광역시

Generated: 2026-05-26 09:23:31 +09:00

## Scope

- Target file: `targets.csv`
- Province/work unit: 대전광역시 (`3000`)
- Allowed sources used: `policy.nec.go.kr`; official guidance reference from `data.go.kr/data/15040587/openapi.do`
- Rejected source classes: party, candidate campaign, news, private, and non-government sources were not used.

## Method

For each target, I queried the official NEC candidate pledge endpoint with the target election, province/district parameters, then accepted only records matching all of: candidate name, party name, district name/code, candidate ID, and requested document type. Generic guidance was treated as guidance-only and was not written as a hit.

Official endpoint queried: `https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do`

## Counts

- Target rows reviewed: 24
- Candidate-specific official structured records matched: 24
- Direct official PDF document hits recovered: 0
- Official structured records with requested document still lacking a file path: 24
- No official candidate-specific record found: 0
- Unique official query batches: 11
- Official guidance-only sources consulted: 1

## Result

No target produced a direct official PDF URL for the requested missing document. All 24 matched targets are represented in official_hits.jsonl as candidate-specific NEC structured records; their requested document segment has an empty file path and status official_structured_record_no_document.

## Changed files

- `official_hits.jsonl`
- `agent_report.md`
