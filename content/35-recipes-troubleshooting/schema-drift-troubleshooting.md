---
schema_version: 1
id: DBKB-REC-0037
title: Schema Drift Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [data-contracts, integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0036]
related: [DBKB-CONTRACT-0006]
aliases: [schema drift runbook]
search_keywords: [schema drift, unexpected column, type change, contract break, compatibility]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000095, SRC-000096]
acceptance_criteria: [Drift detection, impact, containment, compatibility and remediation are covered]
---
# Schema Drift Troubleshooting

Capture source/target schema revision, first observed timestamp, field/type/nullability/enum diff, producer build, consumer matrix és failing payload. Classify additive, breaking, semantic vagy undocumented change-ként.

Containment: stop publish vagy route quarantine-ba, activate compatible reader/producer, then backfill or migration. Update contract registry, tests, lineage and owner; resume csak consumer evidence és rollback plan után.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
