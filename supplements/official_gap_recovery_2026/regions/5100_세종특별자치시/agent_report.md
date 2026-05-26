# Official gap recovery - 세종특별자치시

Date checked: 2026-05-26

## Scope

- Target file read: `targets.csv` in this directory only.
- Files written: `agent_report.md`, `official_hits.jsonl`.
- Source policy: official institutional sources only.
- Target document type for all rows: `선거공약서`.

## Counts

- Targets reviewed: 6
- Candidate-specific official structured records found: 6
- Downloadable official `선거공약서` PDF hits recovered: 0
- Official guidance-only sources consulted: 1
- Non-official sources accepted: 0

## Official sources checked

- `https://policy.nec.go.kr/plc/commiment/initUCACommiment.do?menuId=CNDDT25`
- `https://policy.nec.go.kr/plc/commiment/initUCACommimentRegion.do`
- `https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do`
- `https://cdn.nec.go.kr/policy_pdf/20260603/PDF/PRMS_DOC_PUB/5100/004_{huboid}_{date}_{seq}.pdf`
- `https://www.data.go.kr/data/15040587/openapi.do` was used as guidance only because it is not candidate-specific.

## Method

For each target, I checked the official NEC candidate promise page and JSON endpoint using `sgId=20260603`, `hRegionId=5100`, the target `subSgId`, and target `sgTypecode`. I then isolated the candidate by `huboid` and inspected the candidate-specific `fileinfo` entry for `선거공약서`.

I also probed the NEC CDN `PRMS_DOC_PUB/5100/004_{huboid}_{date}_{seq}.pdf` pattern for each target from `20260515` through `20260526`, sequences `1` through `5`. No target candidate returned HTTP 200 for `선거공약서`.

## Findings

| target_source_id | election | candidate | party | district | official structured result | downloadable PDF |
|---|---|---:|---|---|---|---|
| candidate-doc:100161690:2 | 시·도지사선거 | 최민호 | 국민의힘 | 세종특별자치시 | `선거공약서||||||0||HEIGHT||Y||||00` | no |
| candidate-doc:100158883:2 | 시·도지사선거 | 하헌휘 | 개혁신당 | 세종특별자치시 | `선거공약서||||||0||HEIGHT||Y||||00` | no |
| candidate-doc:100153756:2 | 교육감선거 | 강미애 | 무소속 | 세종특별자치시 | `선거공약서||||||0||HEIGHT||Y||||00` | no |
| candidate-doc:100153760:2 | 교육감선거 | 안광식 | 무소속 | 세종특별자치시 | `선거공약서||||||0||HEIGHT||Y||||00` | no |
| candidate-doc:100153758:2 | 교육감선거 | 임전수 | 무소속 | 세종특별자치시 | `선거공약서||||||0||HEIGHT||Y||||00` | no |
| candidate-doc:100153759:2 | 교육감선거 | 원성수 | 무소속 | 세종특별자치시 | `선거공약서||||||0||HEIGHT||Y||||00` | no |

## Conclusion

All six targets have candidate-specific official NEC structured records, but the `선거공약서` file path is blank in every record. The same candidates have other official document entries such as `선거공보` and `5대공약`, but those are not the requested document type and were not accepted as recovered `선거공약서` PDFs.
