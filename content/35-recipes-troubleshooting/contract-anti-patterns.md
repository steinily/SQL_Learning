---
schema_version: 1
id: DBKB-REC-0052
title: Contract Anti-Patterns
type: error
primary_domain: recipes
secondary_domains: [data-contracts, integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0051]
related: [DBKB-CONTRACT-0001]
aliases: [contract mistakes]
search_keywords: [breaking schema, no owner, undocumented event, version drift, no consumer test]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Contract anti-patterns include detection and compatibility remediation]
---
# Contract Anti-Patterns

Anti-pattern az undocumented event/endpoint, schema owner nélkül, generated spec runtime enforcement nélkül, consumer test hiánya, silent breaking change, version/sunset nélkül és `id/source/type` nélküli event.

Detectáld registry coverage, compatibility diff, consumer failure, unknown event és contract freshness alapján. Remediation contract-first publish gate, examples/test evidence, impact analysis, dual-run és deprecation communication.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
