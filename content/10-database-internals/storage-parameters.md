---
schema_version: 1
id: DBKB-INT-0020
title: Storage Parameters
type: reference
primary_domain: database-internals
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0002]
related: [DBKB-INT-0022]
aliases: [relation storage settings]
search_keywords: [storage parameter, fillfactor, autovacuum table setting]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Storage parameters scopeját, impactját és rollbackjét dokumentálja]
---
# Storage Parameters

Relation- és index-level storage parameters, például `fillfactor` vagy autovacuum setting, workload-specific trade-offot adnak. Módosítás előtt baseline, maintenance window és rollback plan szükséges.

## Források
- [PostgreSQL 18 — Storage Parameters](https://www.postgresql.org/docs/18/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS)
