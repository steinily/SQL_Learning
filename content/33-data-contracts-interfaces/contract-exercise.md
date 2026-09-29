---
schema_version: 1
id: DBKB-CONTRACT-0012
title: Contract Exercise
type: exercise
primary_domain: data-contracts
secondary_domains: [integration, testing]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CONTRACT-0011]
related: [DBKB-CONTRACT-0006, DBKB-CONTRACT-0007]
aliases: [contract lab]
search_keywords: [data contract exercise, schema evolution, CDC, consumer test]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Learner produces HTTP and event contracts, compatibility tests and governance evidence]
---
# Contract Exercise

Tervezd meg egy order API és order-created event contractját.

1. Készíts OpenAPI operationt request/response/error/security leírással.
2. Készíts AsyncAPI message-t és CloudEvents envelope-t idempotency, ordering, replay és schema version mezőkkel.
3. Írj producer/consumer compatibility teszteket valid, invalid, null, unknown-field és duplicate példákkal.
4. Adj deprecation, governance, threat review és rollback tervet.

Elvárt eredmény: contract files, diff report, test evidence, consumer matrix és publish decision. Execution-verified állítást csak ténylegesen futtatott validator outputtal használj.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
