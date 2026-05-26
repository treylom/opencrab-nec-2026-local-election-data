# Official gap recovery report - 경상북도

- Target file: `targets.csv`
- Official sources used: `policy.nec.go.kr` candidate/party pledge endpoint and `cdn.nec.go.kr` official PDF files referenced by that endpoint.
- Rejected sources: party, candidate, news, private, or non-government sources were not used.
- Match rule: candidate rows require official NEC record match on `huboid + candidate + party` and exact target `doc_type`; proportional party rows require official NEC record match on `party + district` and a displayed official party PDF record.

## Counts

- Targets checked: 142
- Official hits accepted: 0
- No accepted hit: 142
- Official query groups checked: 64

| Target document type | Targets | Hits | No hit |
|---|---:|---:|---:|
| 5대공약 | 2 | 0 | 2 |
| 비례대표 정당 제출자료 | 22 | 0 | 22 |
| 선거공보 | 61 | 0 | 61 |
| 선거공약서 | 57 | 0 | 57 |

## Accepted hits

| record_id | district | candidate/party | target_doc_type | official_doc_type | official_url |
|---|---|---|---|---|---|
| - | - | - | - | - | - |

## Notes

- Generic forms or guidance pages were not counted as hits.
- Candidate-specific official records where the exact document type had an empty path, `0||`, or was not displayed were counted as no hit.
- URLs in `official_hits.jsonl` were accepted only after the official PDF URL returned HTTP 200.
