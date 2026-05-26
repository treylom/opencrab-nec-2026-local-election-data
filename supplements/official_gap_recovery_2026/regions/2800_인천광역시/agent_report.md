# Official-source recovery report: 인천광역시 (2800)

Run date: 2026-05-26 KST

## Scope

- Target file read: `targets.csv`
- Files written: `agent_report.md`, `official_hits.jsonl`
- Province/work unit: 인천광역시
- Accepted sources: official institutional sources only. Recovery checks used the NEC policy site structured records at `policy.nec.go.kr`.

## Method

- Queried `https://policy.nec.go.kr/plc/commiment/initUCACommimentList.do` through the live NEC policy page session.
- Candidate records were matched exactly by `huboid`, election type, district, and requested document type.
- Party proportional records were matched exactly by `jdid`, party name, district, election type, and requested document slot.
- A hit required a candidate/party-specific official record with a non-empty official file path and public display status where applicable.
- Generic NEC submission forms or guidance pages were treated as `official_guidance_only` and not counted as hits.

## Counts

- Targets checked: 65
- Official NEC query groups: 27
- Official target identities matched: 65
- Candidate-document targets: 54
- Party-document targets: 11
- Accepted official hits: 0
- Rejected/non-hit official records: 65
- Missing official identities: 0

## Result

No recoverable candidate- or party-specific official policy document was found for the target rows. Every target matched an official NEC structured record, but the requested document slot was either blank/no file path or not publicly displayed. `official_hits.jsonl` is intentionally empty.