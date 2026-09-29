---
schema_version: 1
id: DBKB-PG-0026
title: Extensions Management
type: playbook
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
prerequisites: [DBKB-PG-0014]
related: [DBKB-PG-0027]
aliases: [extension lifecycle]
search_keywords: [extension management, extension upgrade, extension dependency]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Inventory, compatibility, rollout, rollback és drift check steps]
---
# Extensions Management

Extension lifecycle: inventory és version pin; dependency/engine compatibility; staging migration; rollout; health check; rollback vagy restore. `CREATE EXTENSION` és `ALTER EXTENSION UPDATE` minden target database-en külön state-et hozhat létre.

## Források
- [PostgreSQL 18 — Extension Building Infrastructure](https://www.postgresql.org/docs/18/extend-extensions.html)
