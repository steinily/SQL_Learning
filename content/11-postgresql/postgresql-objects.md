---
schema_version: 1
id: DBKB-PG-0007
title: PostgreSQL Objects
type: reference
primary_domain: postgresql
secondary_domains: [database]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0006]
related: [DBKB-PG-0016, DBKB-PG-0018]
aliases: [database object types]
search_keywords: [table, index, view, sequence, function, PostgreSQL object]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Table, index, view, sequence, function és extension object scopeját sorolja]
---
# PostgreSQL Objects

PostgreSQL object típusok közé tartozik table, index, view, materialized view, sequence, function, procedure, type és extension. Ownership, dependency és privilege metadata alapján kell lifecycle-t és deployment ordert tervezni.

## Források
- [PostgreSQL 18 — SQL Commands](https://www.postgresql.org/docs/18/sql-commands.html)
