# Official gap recovery report - ???

- Target file: `targets.csv`
- Official source used: `policy.nec.go.kr` candidate pledge structured JSON (`initUCACommimentList.do`) and official download endpoint (`/plc/common/downloadFile.do`).
- Source policy: only `*.nec.go.kr` official records were used; party/candidate/news/private sources were rejected by not querying them.

## Counts
- Targets searched: 276
- Official API groups queried: 116
- Matched official candidate/party records: 276
- Hits written: 0
- Candidate-document hits: 0
- Party proportional hits: 0
- No-hit targets: 276
- Official query errors: 0

## Hits by target document type
- None

## Hits by election type
- None

## No-hit reasons
- matched_official_record_but_target_doc_unavailable: 276

## Method notes
- For candidate targets, records were matched by `huboid`, with district and party consistency checks where present, then by target document type (`????` also allowed official label `???????`).
- For proportional party targets, records were matched by `sggname` + `jdname`; NEC exposes these submissions as `????` files in the candidate pledge UI.
- A hit required a candidate/party-specific official record with a non-empty PDF path and `fileDispYn=Y`. Generic guidance/forms were not counted.
