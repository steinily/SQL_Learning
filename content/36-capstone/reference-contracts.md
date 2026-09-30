---
schema_version: 1
id: DBKB-CAP-0067
title: Reference Contracts
type: reference
primary_domain: capstone
secondary_domains: [data-contracts, integration]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0066]
related: [DBKB-CONTRACT-0001]
aliases: [contract checklist]
search_keywords: [contract reference, schema, compatibility, security, consumer]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Contract design, validation, compatibility, security and lifecycle checklist is provided]
---
# Reference Contracts

Checklist: owner/consumer; schema/semantics/examples; auth/classification; quality/SLO; idempotency/order/replay; compatibility; revision/sunset; registry; static/runtime tests; observability; rollback.

OpenAPI operation, AsyncAPI channel/message és CloudEvents context csak runtime mapping és actual validator evidence mellett tekinthető enforcednek.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
