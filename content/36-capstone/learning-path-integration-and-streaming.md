---
schema_version: 1
id: DBKB-CAP-0077
title: Learning Path Integration and Streaming
type: learning-path
primary_domain: capstone
secondary_domains: [data-integration, streaming]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, apache-kafka]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0076]
related: [DBKB-CAP-0032, DBKB-CAP-0033]
aliases: [integration streaming path]
search_keywords: [integration learning path, streaming, AsyncAPI, Kafka, replay]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000087, SRC-000095, SRC-000096]
acceptance_criteria: [Ordered API/event contract, delivery, replay, compatibility and observability milestones]
---
# Learning Path Integration and Streaming

Sorrend: OpenAPI/AsyncAPI → message schema/CloudEvents → producer/consumer test → topic/partition/offset → lag/replay/DLQ → reconciliation → integration/streaming exercises/cases.

Exit criteria: idempotency, ordering/delivery scope, contract compatibility, lag/alert, bounded replay és evidence-backed recovery.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
