# NEC 2026 Local Election Policy Data for OpenCrab

This repository contains Markdown documents converted from official National Election Commission policy and pledge materials for OpenCrab ingest.

- Source site: https://policy.nec.go.kr/
- OpenCrab GitHub ingest path for all documents: atches
- Fallback per-batch ingest paths: atches/batch_001 through atches/batch_065
- Each batch contains at most 100 Markdown documents.
- Audit metadata is in metadata/ and is outside the recommended OpenCrab ingest path.

The dataset intentionally excludes the earlier graph pack. OpenCrab should ingest these as readable Markdown source documents and derive ontology data from the documents.
