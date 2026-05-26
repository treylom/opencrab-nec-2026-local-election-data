# Official Gap Recovery Report - 부산광역시

## Scope
- Target file read: 	argets.csv
- Files written: gent_report.md, official_hits.jsonl
- Province/work unit: 부산광역시 (2600)
- Official sources used: policy.nec.go.kr candidate commitment page and initUCACommimentList.do structured API.
- Rejected source classes: party/candidate/news/private sources; generic NEC guidance was not counted as a hit.

## Result Counts
- Targets checked: 152
- Candidate-specific official records matched: 135
- Party/district official records matched: 17
- Recoverable official PDF hits: 0
- Official structured records found but target document file/path unavailable: 152
- Missing exact official structured record: 0
- Official API query groups: 61

## Counts By Target Document Type
| Document type | Targets | PDF hits |
|---|---:|---:|
| 비례대표 정당 제출자료 | 17 | 0 |
| 선거공보 | 92 | 0 |
| 선거공약서 | 43 | 0 |

## No-Hit Reasons
- official_record_file_path_empty: 152

## Notes
All 152 targets had an exact candidate/party-specific official NEC structured record. None had a downloadable file path for the target document type at the time of recovery. Therefore official_hits.jsonl intentionally contains 0 records.