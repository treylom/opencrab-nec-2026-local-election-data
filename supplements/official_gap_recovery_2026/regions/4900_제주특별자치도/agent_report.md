# 제주특별자치도 official gap recovery report

- Work unit: 4900_제주특별자치도
- Target file read: `targets.csv`
- Official sources used: `policy.nec.go.kr` candidate pledge page/API; `data.go.kr` NEC election pledge API metadata for official service scope.
- Source restrictions applied: no party, candidate, news, or private sources accepted.
- Search template applied per target: exact candidate + party + district + document type, then matched through the official NEC candidate pledge endpoint using `sgId=20260603`, target `subSgId`, `hRegionId=4900`, target `sgTypecode`, and target `sggid` where district-level selection was required.

## Counts

| Metric | Count |
|---|---:|
| Targets reviewed | 14 |
| Candidate/party/district official structured records matched | 14 |
| Accepted official PDF/document URLs recovered | 0 |
| Official structured records with target document path empty | 14 |
| Official guidance-only records accepted as hits | 0 |
| Non-official sources accepted | 0 |

## Findings

All 13 targets were found as candidate-specific official NEC structured records. For every target document type, the official `fileinfo` segment has an empty document path and `image_count=0`; therefore no candidate-specific public PDF/document URL was recovered. The records are preserved in `official_hits.jsonl` as `official_structured_record_no_public_file` rather than document hits.

| Record ID | Candidate | Party | District | Doc type | Official status |
|---|---|---|---|---|---|
| 320260603-4900-제주특별자치도-100163197-2-선거공약서 | 위성곤 | 더불어민주당 | 제주특별자치도 | 선거공약서 | official_structured_record_no_public_file |
| 320260603-4900-제주특별자치도-100157851-2-선거공약서 | 문성유 | 국민의힘 | 제주특별자치도 | 선거공약서 | official_structured_record_no_public_file |
| 320260603-4900-제주특별자치도-100153886-2-선거공약서 | 양윤녕 | 무소속 | 제주특별자치도 | 선거공약서 | official_structured_record_no_public_file |
| 520260603-4900-제주특별자치도-제주시-일도1동-이도1동-건입동선거구-100162508-1-선거공보 | 한권 | 더불어민주당 | 제주특별자치도 제주시 일도1동·이도1동·건입동선거구 | 선거공보 | official_structured_record_no_public_file |
| 520260603-4900-제주특별자치도-제주시-이도2동갑선거구-100163106-1-선거공보 | 김기환 | 더불어민주당 | 제주특별자치도 제주시 이도2동갑선거구 | 선거공보 | official_structured_record_no_public_file |
| 520260603-4900-제주특별자치도-제주시-화북동선거구-100157833-1-선거공보 | 강성의 | 더불어민주당 | 제주특별자치도 제주시 화북동선거구 | 선거공보 | official_structured_record_no_public_file |
| 520260603-4900-제주특별자치도-제주시-삼양동-봉개동선거구-100155671-1-선거공보 | 박안수 | 더불어민주당 | 제주특별자치도 제주시 삼양동·봉개동선거구 | 선거공보 | official_structured_record_no_public_file |
| 520260603-4900-제주특별자치도-제주시-아라동갑선거구-100154766-1-선거공보 | 김봉현 | 더불어민주당 | 제주특별자치도 제주시 아라동갑선거구 | 선거공보 | official_structured_record_no_public_file |
| 520260603-4900-제주특별자치도-제주시-애월읍을선거구-100161045-1-선거공보 | 강봉직 | 더불어민주당 | 제주특별자치도 제주시 애월읍을선거구 | 선거공보 | official_structured_record_no_public_file |
| 520260603-4900-제주특별자치도-서귀포시-대천동-중문동-예래동선거구-100158090-1-선거공보 | 임정은 | 더불어민주당 | 제주특별자치도 서귀포시 대천동·중문동·예래동선거구 | 선거공보 | official_structured_record_no_public_file |
| 520260603-4900-제주특별자치도-서귀포시-남원읍선거구-100162785-1-선거공보 | 송영훈 | 더불어민주당 | 제주특별자치도 서귀포시 남원읍선거구 | 선거공보 | official_structured_record_no_public_file |
| 1120260603-4900-제주특별자치도-100153761-2-선거공약서 | 송문석 | 무소속 | 제주특별자치도 | 선거공약서 | official_structured_record_no_public_file |
| 1120260603-4900-제주특별자치도-100156980-2-선거공약서 | 고의숙 | 무소속 | 제주특별자치도 | 선거공약서 | official_structured_record_no_public_file |
| 1120260603-4900-제주특별자치도-100162806-2-선거공약서 | 김광수 | 무소속 | 제주특별자치도 | 선거공약서 | official_structured_record_no_public_file |

## Changed files

- `official_hits.jsonl`
- `agent_report.md`
