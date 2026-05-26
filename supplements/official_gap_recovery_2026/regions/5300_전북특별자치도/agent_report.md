# Official Gap Recovery Agent Report - 5300_전북특별자치도

- Run date: 2026-05-26
- Target file: `targets.csv`
- Outputs: `agent_report.md`, `official_hits.jsonl`
- Province/work unit: 전북특별자치도

## Official sources used

- `https://policy.nec.go.kr/plc/commiment/initUCACommiment.do?menuId=CNDDT25`
- `https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do`
- `https://policy.nec.go.kr/js/common.js?v=20240222`

No party, candidate, news, private, or non-official sources were used. Generic guidance or submission forms were not counted as hits.

## Method

Queried the official NEC policy/candidate pledge JSON endpoint for the assigned province (`hRegionId=5300`) and the seven target election subtypes. Each target was exact-matched back to official records by `subSgId`, district, candidate `huboid` or party name, and target document type. A hit required a candidate/party-specific official PDF path in `fileinfo` or `filePathName + updtFileName`.

## Counts

- Target rows searched: 171
- Official rows read from policy.nec.go.kr: 428
- Exact official candidate/party records located: 171
- Accepted official document hits: 0
- Rows with exact official record but no target PDF path: 171
- Rows with no exact official record: 0
- Official guidance-only hits: 0
- Rejected non-official sources: 0

## Counts by document type

| Document type | Targets | Hits | No recoverable official file |
|---|---:|---:|---:|
| 5대공약 | 2 | 0 | 2 |
| 비례대표 정당 제출자료 | 16 | 0 | 16 |
| 선거공보 | 108 | 0 | 108 |
| 선거공약서 | 45 | 0 | 45 |

## Official query coverage

| subSgId | sgTypecode | official total | rows read | pages |
|---|---:|---:|---:|---:|
| 1120260603 | 11 | 2 | 2 | 1 |
| 320260603 | 3 | 5 | 5 | 1 |
| 420260603 | 4 | 40 | 40 | 3 |
| 520260603 | 5 | 54 | 54 | 4 |
| 620260603 | 6 | 290 | 290 | 20 |
| 820260603 | 8 | 7 | 7 | 1 |
| 920260603 | 9 | 30 | 30 | 1 |

## Result

No accepted official document hits were recovered for this work unit. The official NEC records were present for all 171 targets, but the target document slots were empty/disabled in the official structured data (for example, empty `fileinfo` paths or party `fileDispYn=N`). `official_hits.jsonl` is intentionally empty.
