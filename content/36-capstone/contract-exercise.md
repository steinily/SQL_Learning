---
schema_version: 1
id: DBKB-CAP-0044
title: Contract Exercise
type: exercise
primary_domain: capstone
secondary_domains: [data-contracts, integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0043]
related: [DBKB-CONTRACT-0001]
aliases: [contract lab]
search_keywords: [contract exercise, OpenAPI, AsyncAPI, compatibility, consumer]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Learner creates API/event contract, compatibility tests, security and deprecation plan]
---
# Contract Exercise

Order create API/eventhez készíts OpenAPI, AsyncAPI és CloudEvents contractot schema/semantics, security, idempotency, ordering, replay és error behavior értékekkel.

Írj producer/consumer compatibility teszteket breaking/non-breaking diffre, unknown/duplicate payloadra és deprecationre. Evidence: validator/test output, consumer matrix, registry revision és rollback.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
