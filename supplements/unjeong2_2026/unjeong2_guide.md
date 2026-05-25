---
title: 운정2동 2026 지방선거 OpenCrab 보강
source_site: https://policy.nec.go.kr/
district_mapping_source: https://gg.nec.go.kr/gg/main/contents.do?guSiGunId=ggpaju&menuNo=1000271
generated_at: 2026-05-25T22:54:15.400Z
---

# 운정2동 2026 지방선거 OpenCrab 보강

이 문서는 기존 OpenCrab 팩의 누락처럼 보이는 부분을 설명하기 위한 보강 문서입니다. 결론은 단순합니다. 경기도지사, 경기도교육감, 파주시장 9명의 5대공약 문서는 GitHub와 OpenCrab에 들어가 있습니다. 반면 운정2동 실제 지역구인 파주시제2선거구와 파주시나선거구 후보들의 선거공보, 그리고 비례대표 정당 제출자료는 공식 API 기준으로 다운로드 가능한 PDF 경로가 없습니다.

운정2동 선거구 매핑은 파주시선거관리위원회 선거관리현황을 기준으로 했습니다. 운정2동은 도의원 선거에서는 파주시제2선거구, 시의원 선거에서는 파주시나선거구입니다.

## 상태 요약

| 선거 |대상 |상태 |OpenCrab |
| --- | --- | --- | --- |
| 경기도지사 | 경기도 | 5명 5대공약 문서 있음 | 문서 노드 5건 확인 |
| 경기도교육감 | 경기도 | 2명 5대공약 문서 있음 | 문서 노드 2건 확인 |
| 파주시장 | 파주시 | 2명 5대공약 문서 있음 | 문서 노드 2건 확인 |
| 경기도의원 | 파주시제2선거구 | 후보 2명, 선거공보 PDF 경로 없음 | 문서 노드 없음이 정상 |
| 파주시의원 | 파주시나선거구 | 후보 5명, 선거공보 PDF 경로 없음 | 문서 노드 없음이 정상 |
| 경기도의원 비례 | 경기도 | 20개 정당, 다운로드 PDF 경로 없음 | 메타데이터 보강 필요 |
| 파주시의원 비례 | 파주시 | 2개 정당, 다운로드 PDF 경로 없음 | 메타데이터 보강 필요 |

## OpenCrab에 이미 있는 5대공약 문서

| 선거 |후보 |정당 |문서 |source_id |
| --- | --- | --- | --- | --- |
| 경기도지사 | 추미애 | 더불어민주당 | 5대공약 | candidate-doc:100163148:3 |
| 경기도지사 | 양향자 | 국민의힘 | 5대공약 | candidate-doc:100163432:3 |
| 경기도지사 | 조응천 | 개혁신당 | 5대공약 | candidate-doc:100163471:3 |
| 경기도지사 | 홍성규 | 진보당 | 5대공약 | candidate-doc:100153796:3 |
| 경기도지사 | 김현욱 | 국민연합 | 5대공약 | candidate-doc:100158402:3 |
| 경기도교육감 | 임태희 | 무소속 | 5대공약 | candidate-doc:100163064:3 |
| 경기도교육감 | 안민석 | 무소속 | 5대공약 | candidate-doc:100153797:3 |
| 파주시장 | 손배찬 | 더불어민주당 | 5대공약 | candidate-doc:100154507:3 |
| 파주시장 | 박용호 | 국민의힘 | 5대공약 | candidate-doc:100156661:3 |

## 공식 문서 PDF가 없는 운정2동 지역구 후보

| 선거 |후보 |정당 |문서상태 |공식 fileinfo |
| --- | --- | --- | --- | --- |
| 경기도의원 파주시제2선거구 | 손희정 | 더불어민주당 | unavailable_official_source | 선거공보\|\|\|\|\|\|0\|\|HEIGHT\|\|Y\|\|\|\|00 |
| 경기도의원 파주시제2선거구 | 김광선 | 국민의힘 | unavailable_official_source | 선거공보\|\|\|\|\|\|0\|\|HEIGHT\|\|Y\|\|\|\|00 |
| 파주시의원 파주시나선거구 | 김경옥 | 더불어민주당 | unavailable_official_source | 선거공보\|\|\|\|\|\|0\|\|HEIGHT\|\|Y\|\|\|\|00 |
| 파주시의원 파주시나선거구 | 이정은 | 더불어민주당 | unavailable_official_source | 선거공보\|\|\|\|\|\|0\|\|HEIGHT\|\|Y\|\|\|\|00 |
| 파주시의원 파주시나선거구 | 옥승철 | 국민의힘 | unavailable_official_source | 선거공보\|\|\|\|\|\|0\|\|HEIGHT\|\|Y\|\|\|\|00 |
| 파주시의원 파주시나선거구 | 최창호 | 국민의힘 | unavailable_official_source | 선거공보\|\|\|\|\|\|0\|\|HEIGHT\|\|Y\|\|\|\|00 |
| 파주시의원 파주시나선거구 | 소경준 | 노동당 | unavailable_official_source | 선거공보\|\|\|\|\|\|0\|\|HEIGHT\|\|Y\|\|\|\|00 |

## 비례대표 정당 메타데이터 상태

| 선거 |정당 |문서상태 |공식 fileinfo |
| --- | --- | --- | --- |
| 경기도의원 비례대표 | 더불어민주당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 국민의힘 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 조국혁신당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 개혁신당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 진보당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 기본소득당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 사회민주당 | unavailable_official_source | 0\|\| |
| 경기도의원 비례대표 | 거지당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 공화당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 국민대통합당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 국민연합 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 기독당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 대한국민당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 새미래민주당 | unavailable_official_source | 0\|\| |
| 경기도의원 비례대표 | 자유와혁신 | unavailable_official_source | 0\|\| |
| 경기도의원 비례대표 | 정의당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 친미연합 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 국민당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 한국독립당 | unavailable_official_source | 1\|\|HEIGHT |
| 경기도의원 비례대표 | 한나라당 | unavailable_official_source | 1\|\|HEIGHT |
| 파주시의원 비례대표 | 더불어민주당 | unavailable_official_source | 0\|\| |
| 파주시의원 비례대표 | 국민의힘 | unavailable_official_source | 0\|\| |

## 해석

- 이 보강 데이터는 누락된 공약 내용을 만들지 않습니다.
- 공식 원천에서 다운로드 가능한 PDF 경로가 없는 항목은 `unavailable_official_source`로 표시합니다.
- 향후 선관위가 새 PDF를 공개하면 재수집 후 이 보강 데이터의 상태를 갱신해야 합니다.
- 현재 HTML 가이드나 공익 서비스에서는 9명의 5대공약은 내용 카드로 보여주고, 나머지 지역구/비례 항목은 후보 또는 정당 메타데이터와 공식 문서 미제공 상태를 함께 보여주는 것이 정확합니다.
