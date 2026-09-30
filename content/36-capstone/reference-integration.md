---
schema_version: 1
id: DBKB-CAP-0058
title: Reference Integration
type: reference
primary_domain: capstone
secondary_domains: [data-integration, contracts]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, apache-kafka]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0057]
related: [DBKB-INTG-0001]
aliases: [integration checklist]
search_keywords: [integration reference, API, event, retry, idempotency, reconciliation]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000087, SRC-000095, SRC-000096]
acceptance_criteria: [Integration contract, transport, error, retry, quarantine and validation checklist is provided]
---
# Reference Integration

Checklist: API/event contract; auth; schema/version; idempotency; timeout/backoff; ordering; duplicate/replay; DLQ/quarantine; rate/quota; observability; consumer compatibility; reconciliation; ownership; rollback.

Transport delivery is not target correctness; preserve accepted/rejected/duplicate counts and business invariant evidence.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
