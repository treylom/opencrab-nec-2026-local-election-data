# Official Gap Recovery Report - 2900_전남광주통합특별시

## Scope
- Target file read: 	argets.csv in this directory only.
- Files written: official_hits.jsonl, gent_report.md.
- Region/work unit kept as 전남광주통합특별시, separate from 광주광역시 and 전라남도.
- Source policy: official institutional sources only; no party, candidate, news, or private sources used.

## Official Sources Queried
- policy.nec.go.kr candidate policy page: https://policy.nec.go.kr/plc/commiment/initUCACommiment.do?menuId=CNDDT25
- policy.nec.go.kr structured list endpoint: https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do

## Method
- Queried the official CNDDT25 candidate-policy list for sgId=20260603, hRegionId=2900, and each target subSgId/sgTypecode/sggid where applicable.
- Matched candidate targets by huboid; matched the proportional party target by jdid.
- Checked the exact target document type only: 선거공약서, 선거공보, or proportional party submission mapped to the official party record.
- Did not count nearby official documents such as 5대공약 or a different document label as recovered hits for the target type.

## Results
- Targets searched: 20
- Official candidate/party-specific structured records found: 20
- Exact official PDF/document hits recovered: 0
- Exact target document listed but no official file path/download URL: 20
- Official structured record found but exact target type not listed: 0
- No official record found: 0
- Official guidance-only sources counted as hits: 0

## Target Breakdown
- 시·도지사선거 선거공약서: 5
- 시·도의회의원선거 선거공보: 11
- 광역의원비례대표선거 party record: 14
- 교육감선거 선거공약서: 3

## Conclusion
All 20 targets have official candidate/party-specific structured records on policy.nec.go.kr, but none expose an exact target-document PDF path or download URL at the time checked. The JSONL records preserve the exact official query terms, endpoint parameters, and the official raw file metadata showing the missing path state.