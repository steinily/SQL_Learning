---
schema_version: 1
id: DBKB-CAP-0032
title: Integration Exercise
type: exercise
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
prerequisites: [DBKB-CAP-0031]
related: [DBKB-INTG-0001]
aliases: [integration lab]
search_keywords: [integration exercise, API, event, idempotency, replay]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000095, SRC-000096]
acceptance_criteria: [Learner creates API/event contract, retry, quarantine and reconciliation tests]
---
# Integration Exercise

Készíts OpenAPI és AsyncAPI contractot customer update flow-ra, valid/invalid payloadokkal, idempotency key-jel, retry/DLQ és reconciliation ellenőrzéssel.

Teszteld duplicate, out-of-order, timeout, schema drift és downstream rejection esetét. Evidence: contract diff, validator/test output, lag, rejected/accepted counts és recovery runbook.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
