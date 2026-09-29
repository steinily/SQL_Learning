---
schema_version: 1
id: DBKB-CONTRACT-0007
title: Contract Testing
type: technology
primary_domain: data-contracts
secondary_domains: [testing, integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CONTRACT-0006]
related: [DBKB-TEST-0001]
aliases: [schema contract test]
search_keywords: [contract test, schema validation, compatibility check, consumer test]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000095, SRC-000096]
acceptance_criteria: [Producer, consumer, schema and compatibility test stages with evidence are defined]
---
# Contract Testing

Contract test ellenőrizze a producer outputot és a consumer elvárását representative valid/invalid examples-szel. A pipeline stage tartalmazzon lint, schema validation, compatibility diff, generated artifact check és runtime integration testet.

A passing static diff nem bizonyítja a semantic compatibilityt: teszteld error, null, unknown field, ordering, retry és version transition esetét is. Tartsd meg a test input/output evidence-et, tool versiont és contract revisiont.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
