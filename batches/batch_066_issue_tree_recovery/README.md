# Pledge Issue Tree Structured Recovery Batch

- Source: NEC policy pledge issue tree data
- Official report URL: https://policy.nec.go.kr/js/pdfViewer/web/260331_SurveyPolicyIssue.pdf
- Recovery reason: the original issue-tree PDF-derived Markdown had broken Korean text and was skipped by OpenCrab GitHub ingest, so this batch adds readable parsed CSV data plus region-level Markdown documents.
- Survey1 issue-tree rows: 2632
- Survey9 keyword-ranking rows: 1605
- Regions: 17

## Files

- `tables/survey1_issue_tree.csv`: region, main_category, middle_category, sub_category, keyword
- `tables/survey9_keyword_rankings.csv`: region, policy_issue, rank, weight, issue keyword
- `documents/survey1_by_region/*.md`: region-level issue tree hierarchy
- `documents/survey9_by_region/*.md`: region-level policy issue keyword rankings

## Regions

- 강원: survey1 144 rows, survey9 93 rows
- 경기: survey1 162 rows, survey9 100 rows
- 경남: survey1 158 rows, survey9 96 rows
- 경북: survey1 133 rows, survey9 91 rows
- 광주: survey1 139 rows, survey9 92 rows
- 대구: survey1 132 rows, survey9 90 rows
- 대전: survey1 137 rows, survey9 94 rows
- 부산: survey1 179 rows, survey9 98 rows
- 서울: survey1 160 rows, survey9 100 rows
- 세종: survey1 157 rows, survey9 100 rows
- 울산: survey1 196 rows, survey9 97 rows
- 인천: survey1 168 rows, survey9 100 rows
- 전남: survey1 152 rows, survey9 80 rows
- 전북: survey1 158 rows, survey9 92 rows
- 제주: survey1 151 rows, survey9 92 rows
- 충남: survey1 131 rows, survey9 90 rows
- 충북: survey1 175 rows, survey9 100 rows
