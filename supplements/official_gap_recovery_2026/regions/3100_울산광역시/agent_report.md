# Official Gap Recovery Report - 3100 울산광역시

## Scope

- Target CSV: 	argets.csv
- Election: 제9회 전국동시지방선거 (sgId=20260603)
- Official-source rule applied: policy.nec.go.kr, data.go.kr/data.nec.go.kr, *.nec.go.kr, *.go.kr only.
- Rejected source classes: party/candidate/news/private sources and generic guidance-only pages.

## Search Method

For each target row, I searched the official NEC policy candidate-record endpoint using the exact election/district filters, then matched the exact candidate ID (huboid), party, district, and requested document type.

- Official candidate page: https://policy.nec.go.kr/plc/commiment/initUCACommiment.do?menuId=CNDDT25
- Official structured endpoint used by that page: POST https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do
- Supporting official guidance checked: https://www.data.go.kr/data/15040587/openapi.do

## Counts

- Targets reviewed: 22
- 선거공약서 targets: 18
- 선거공보 targets: 4
- Candidate-specific official NEC records found: 22
- Target document slots found in official records: 22
- Accepted downloadable/structured target-document hits: 0
- Official records with target slot but no file path/content: 22
- Generic guidance-only hits accepted: 0

## Result

No accepted target-document hits were recovered. All 22 targets had candidate-specific official NEC records, but the requested target document slot was empty and contained no downloadable file path or structured document content. Candidate 5대공약 PDFs, where present, were not accepted as substitutes for exact 선거공약서 targets.

## Target-Level Evidence

| Candidate | Party | District | Target doc | Status | fileDispYn | Official doc slot |
|---|---|---|---|---|---|---|
| 김상욱 | 더불어민주당 | 울산광역시 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 김두겸 | 국민의힘 | 울산광역시 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 김종훈 | 진보당 | 울산광역시 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 박맹우 | 무소속 | 울산광역시 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 박태완 | 더불어민주당 | 중구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 고호근 | 무소속 | 중구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 최덕종 | 더불어민주당 | 남구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 임현철 | 국민의힘 | 남구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 방인섭 | 개혁신당 | 남구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 천기옥 | 국민의힘 | 동구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 박문옥 | 진보당 | 동구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 이장우 | 노동당 | 동구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 이동권 | 더불어민주당 | 북구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 박천동 | 국민의힘 | 북구 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 김시욱 | 더불어민주당 | 울주군 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 이순걸 | 국민의힘 | 울주군 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 권수찬 | 새미래민주당 | 남구제3선거구 | 선거공보 | official_record_target_slot_empty | N | <code>선거공보&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 정훈희 | 국민의힘 | 남구라선거구 | 선거공보 | official_record_target_slot_empty | N | <code>선거공보&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 최치환 | 무소속 | 울주군나선거구 | 선거공보 | official_record_target_slot_empty | N | <code>선거공보&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 이원옥 | 무소속 | 울주군나선거구 | 선거공보 | official_record_target_slot_empty | N | <code>선거공보&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 구광렬 | 무소속 | 울산광역시 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |
| 김주홍 | 무소속 | 울산광역시 | 선거공약서 | official_record_target_slot_empty | Y | <code>선거공약서&#124;&#124;&#124;&#124;&#124;&#124;0&#124;&#124;HEIGHT&#124;&#124;Y&#124;&#124;&#124;&#124;00</code> |

## Output

- official_hits.jsonl: 0 JSONL records
- gent_report.md: this report