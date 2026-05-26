# Official Gap Recovery Agent Report: 전라남도

- Work unit: 전라남도 (province_id 4600)
- Target file read: C:\Users\treyl\Documents\Obsidian\Second_Brain\output\nec_2026_local_election_opencrab\github_repo_nec_2026_local_election_opencrab\supplements\official_gap_recovery_2026\regions\4600_전라남도\targets.csv
- Output JSONL: official_hits.jsonl
- Official sources used: policy.nec.go.kr candidate/party pledge structured endpoint and cdn.nec.go.kr PDF URLs exposed by that endpoint
- Source page: https://policy.nec.go.kr/plc/commiment/initUCACommiment.do?menuId=CNDDT25
- Structured endpoint: https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do
- Completed at: 2026-05-26 09:23:10 +09:00

## Counts

- Targets reviewed: 136
- Official PDF hits: 0
- Candidate/party-specific official structured records with no requested PDF path: 136
- Official PDF links failing HEAD validation: 0
- Not found in official structured records: 0

## Status Breakdown

- official_structured_record_no_document: 136

## Document/Status Breakdown

- 비례대표 정당 제출자료, official_structured_record_no_document: 20
- 선거공보, official_structured_record_no_document: 56
- 선거공약서, official_structured_record_no_document: 60

## Notes

- official_pdf_hit means the target matched a candidate/party-specific official structured record and the exposed cdn.nec.go.kr PDF URL returned a successful HEAD response.
- official_structured_record_no_document means the exact candidate/party/district official record exists, but the requested target document slot has no displayed PDF path or fileDispYn=N.
- No party, candidate campaign, news, or private-domain sources were used.