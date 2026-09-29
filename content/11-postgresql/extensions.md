---
schema_version: 1
id: DBKB-PG-0014
title: Extensions
type: technology
primary_domain: postgresql
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0007]
related: [DBKB-PG-0026]
aliases: [CREATE EXTENSION]
search_keywords: [PostgreSQL extension, CREATE EXTENSION, extension version]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Extension lifecycle, versioning, dependencies és rollback kockázatát leírja]
---
# Extensions

Extension database-level objectként extra typeokat, functions vagy operators adhat. Enablement, version upgrade, dependency, packaging és rollback environment-specific; production extension changehez compatibility és restore terv szükséges.

## Források
- [PostgreSQL 18 — Extensions](https://www.postgresql.org/docs/18/extensions.html)
