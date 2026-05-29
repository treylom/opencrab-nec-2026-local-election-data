# 2026 NEC newly available official documents recheck

Generated at: 2026-05-29T08:15:25.870Z

This supplement rechecks records that were previously classified as missing from the official NEC policy site.

## Result

- Previously missing records rechecked: 1,645
- Newly available on NEC: 146
- Still unavailable on NEC: 1,490
- Not found in the current NEC listing: 9

## Correction

Post-upload validation found that the 14 `비례대표 정당 제출자료` rows were unsafe:

- district/party-only matching attached current NEC PDF paths without enough province identity
- the original download/extraction step reused a single `party-doc_920260603_1.*` filename

The corrected authoritative pack for OpenCrab is therefore candidate/election-office documents only:

- Valid candidate/election-office documents: 132
- Excluded party-list rows: 14
- Corrected Cloud Pack ZIP: `opencrab_nec_recheck_candidate_only_corrected_cloud_pack.zip`
- Exclusion list: `excluded_party_document_mismatch.csv`

## OpenCrab-ready files

- `cloud_pack/manifest.json`
- `cloud_pack/cloud/documents.jsonl`
- `cloud_pack/cloud/chunks.jsonl`
- `cloud_pack/graph/nodes.jsonl`
- `cloud_pack/graph/edges.jsonl`
- `direct_nec_downloads/markdown/*.md`

The source policy is official sources only. Every recovered document URL responded as `application/pdf` from `policy.nec.go.kr` during the recheck.
