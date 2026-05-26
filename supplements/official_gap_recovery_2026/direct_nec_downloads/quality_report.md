# PDF Markdown quality report

Generated: 2026-05-26T00:51:55.431Z

PyMuPDF was used as the primary extractor because pypdf produced `/uni....` glyph-name text for several Korean election PDFs. The sampled PyMuPDF outputs contain readable Korean text for candidate pledge PDFs and proportional-party PDFs.

## Summary

- PDF targets: 596
- Downloadable PDFs: 596
- Markdown extraction ok: 595
- Empty text: 1
- Extract errors: 0
- Total pages: 2967
- Total chars: 941039
- Quality flags: {"suspiciously_short_text":100,"ok":495,"empty_text":1}

## Checked samples

| record_id | extract_status | quality_flag | pages | chars | preview |
| --- | --- | --- | --- | --- | --- |
| 1120260603-1100-서울특별시-100161493-2-선거공약서 | ok | ok | 2 | 3240 | # 교육감선거 서울특별시 정근식 선거공약서 ## Page 1 ▲목표: 헌법이 보장하는 무상교육 완성 ▲우선순위: 우선 ▲이행절차: 교육청+지자체 협력 ▲이행기간: 임기 내 ▲재원조달 방안: 교육청+지자체 예산 이 선거공약서는 「공직선거법」 제66조의 규정에 따른 것입니다. 인쇄: 썬프린팅 경기도 파주시 장명산길 103 T |
| 820260603-4400-충청남도-더불어민주당-1-1 | ok | ok | 8 | 2024 | # 광역의원비례대표선거 충청남도 더불어민주당 비례대표 정당 제출자료 ## Page 1 비례대표 충남도의회의원선거 책자형 선거공보 충남은 1번입니다 ## Page 2 대한민국 국가정상화, ## Page 3 대한민국 국가 정상화 일 잘하는 지방정부 - 회복을 넘어 성장으로, 성장을 이어 행복으로! 대한민국은 지금 무너진 상식 |
| 920260603-4400-아산시-더불어민주당-1-1 | ok | ok | 8 | 1271 | # 기초의원비례대표선거 아산시 더불어민주당 비례대표 정당 제출자료 ## Page 1 ## Page 2 대한민국 국가정상화, ## Page 3 대한민국 국가 정상화 일 잘하는 지방정부 - 회복을 넘어 성장으로, 성장을 이어 행복으로! 대한민국은 지금 무너진 상식을 바로 세우고 다시 미래로 나아가고 있습니다. 이제 지방정부도 |
| 420260603-4100-평택시-100153870-1-선거공보 | ok | ok | 12 | 9230 | # 구·시·군의 장선거 평택시 최원용 선거공보 ## Page 1 “이재명 시대의 새로운 평택” 이재명 대통령과 경기도에서 호흡을 맞추며 일하는 방법을 배웠고 정치도 배웠습니다. 중앙정부와 긴밀히 협력해 시민이 체감하는 변화를 만들겠습니다. 일하는 이재명 선거사무소 경기도 평택시 중앙로 280 2층 T 031-666-000 |
| 420260603-4100-수원시-100162275-1-선거공보 | ok | suspiciously_short_text | 1 | 9 | # 구·시·군의 장선거 수원시 정희윤 선거공보 ## Page 1 |
| 620260603-4100-안양시라선거구-100156936-1-선거공보 | ok | ok | 8 | 3481 | # 구·시·군의회의원선거 안양시라선거구 조은석 선거공보 ## Page 1 2 조은석 번은 과 조은석 함께!! 2 책자형 선거공보 안양시의회의원선거 안양시라선거구(석수1·2동·충훈동) ## Page 2 안양시의회의원선거 (안양시라선거구) 기 호 소속정당명 후보자성명 성 별 생년월일 (세) 직 업 학 력 경 력 2 국민의힘  |

Notes: `suspiciously_short_text` means the PDF was downloaded and converted, but the embedded text is short relative to PDF size. These rows should be candidates for OCR fallback if exact text is important.

## Visual render check

Rendered first-page PNG samples are saved under `quality_samples/`.

- `1120260603-1100-서울특별시-100161493-2-선거공약서_page1.png`: visually readable, text extraction also readable.
- `820260603-4400-충청남도-국민의힘-1-1_page1.png`: visually readable proportional-party leaflet sample.
- `420260603-4100-수원시-100162275-1-선거공보_page1.png`: visually readable, but embedded text extraction is short; keep as OCR fallback candidate.
