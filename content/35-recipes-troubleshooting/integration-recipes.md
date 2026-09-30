---
schema_version: 1
id: DBKB-REC-0017
title: Integration Recipes
type: playbook
primary_domain: recipes
secondary_domains: [data-integration, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, openapi, asyncapi]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0016]
related: [DBKB-INTG-0001]
aliases: [data integration runbook]
search_keywords: [integration, API, CDC, idempotency, reconciliation, dead letter]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000087, SRC-000095, SRC-000096]
acceptance_criteria: [Inbound/outbound contract, idempotency, retry, quarantine and reconciliation are actionable]
---
# Integration Recipes

Integration recipe rögzítse source/target contractot, authenticationt, schema/versiont, idempotency key-t, retry/backoffot, timeoutot, rate limitet, orderinget és dead-letter/quarantine pathot.

Mérd a accepted/rejected/duplicate countot, lagot és reconciliation eltérést. Replay csak bounded, idempotent és auditált legyen; a transport „delivered” státusza nem bizonyít target business correctnesset.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
