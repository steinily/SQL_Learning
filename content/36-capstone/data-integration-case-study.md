---
schema_version: 1
id: DBKB-CAP-0009
title: Data Integration Case Study
type: case-study
primary_domain: capstone
secondary_domains: [data-integration, contracts]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, apache-kafka]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0008]
related: [DBKB-INTG-0001]
aliases: [integration case]
search_keywords: [data integration, API, CDC, reconciliation, contract]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000095, SRC-000096]
acceptance_criteria: [Scenario requires API/event contract, idempotency, retry, quarantine and reconciliation]
---
# Data Integration Case Study

Customer updates három source-ból érkeznek REST API-n és event streamen; duplicate, out-of-order és partial failure fordul elő. Tervezz contractot, idempotency key-t, retry/backoffot, dead-letter/quarantine-t, reconciliationt és ownershipet.

Elvárt evidence: message/API examples, compatibility test, lag/error metrics, replay plan és business invariant check. Runtime delivery nem azonos target correctness-szel.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
