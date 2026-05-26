# Official Source Reconnaissance

Generated: 2026-05-26 KST

## Source classes reviewed

| Source class | Official? | Recovery use | Constraint |
| --- | --- | --- | --- |
| `policy.nec.go.kr` | Yes | Canonical PDFs and current publication state for candidate/party policy material | Already queried directly. A missing PDF path here means the current policy API does not expose the document. |
| Public Data Portal candidate pledge API | Yes | Structured candidate pledge text for `sgTypecode` 1, 3, 4, 11 | Requires `ServiceKey`; not a PDF replacement. API docs say it takes `sgId`, `sgTypecode`, and `cnddtId`. |
| Public Data Portal party policy API | Yes | Structured party policy text by election and party | Requires `ServiceKey`; party-level only. |
| `*.nec.go.kr` local election commission boards | Yes | Candidate-specific attachments if present | Search results for 2026 mostly show submission guidance and forms; these are useful provenance but not recovered candidate documents. |
| `*.go.kr` local government, education office, and council sites | Yes | Only if the page/attachment is candidate/party-specific and clearly for the 2026 local election | Expected to be rare because general-purpose local governments are politically neutral and usually do not republish campaign materials. |

## Evidence

- Public Data Portal candidate pledge API: `https://www.data.go.kr/data/15040587/openapi.do`
  - Official provider: National Election Commission.
  - Request endpoint shown in the public documentation: `http://apis.data.go.kr/9760000/ElecPrmsInfoInqireService/getCnddtElecPrmsInfoInqire`.
  - The documentation says the service provides candidate pledge information and uses `sgId`, `sgTypecode`, and `cnddtId`.
  - The same documentation states election pledge-document target types are presidential, metropolitan/provincial governor, municipal head, and superintendent elections.

- Public Data Portal party policy API: `https://www.data.go.kr/data/15040588/openapi.do`
  - Official provider: National Election Commission.
  - Request endpoint shown in the public documentation: `http://apis.data.go.kr/9760000/PartyPlcInfoInqireService/getPartyPlcInfoInqire`.
  - The documentation says party policy information is opened after candidate registration closes, party numbers are finalized, and OCR/review procedures are completed.

- Local NEC board example, Dangjin: `https://cn.nec.go.kr/cn/bbs/B0000264/view.do?category1=cn&category2=cndangjin&deleteCd=0&menuNo=1300155&nttId=284101&pageIndex=1`
  - The post says the commission receives candidate policy material to publish through `https://policy.nec.go.kr`.
  - The post lists PDF submission deadlines and notes proportional local council campaign bulletin PDFs are submitted by the recommending party to the constituency commission.

- Local NEC board example, Yeosu: `https://jn.nec.go.kr/jn/bbs/B0000264/view.do?category1=jn&category2=jnyeosu&deleteCd=0&menuNo=1500061&nttId=284421&pageIndex=1`
  - The post is a 2026 local election submission-form notice.
  - It instructs candidates to submit machine-readable PDF files and includes form/instruction attachments, not candidate-specific recovered documents.

## Working conclusion

The highest-yield official recovery path is not arbitrary local-government search. It is:

1. Reclassify current NEC policy API rows correctly, including proportional PDFs exposed through `filePathName + updtFileName`.
2. Directly download and convert `pack_stale_currently_available` PDFs from `policy.nec.go.kr`.
3. For remaining `current_unavailable_official_source` rows, search `*.nec.go.kr` and `*.go.kr` by province. Accept only candidate/party-specific official attachments or official structured data.
4. Treat local NEC submission-form notices as `official_guidance_only`, not as recovered documents.
5. Use Public Data Portal APIs only when a valid `ServiceKey` is available; without it, classify those rows as `needs_service_key` if the API is the only plausible official structured source.
