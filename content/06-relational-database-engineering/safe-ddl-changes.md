---
schema_version: 1
id: DBKB-RDBE-0015
title: Safe DDL Changes
type: playbook
primary_domain: relational-database-engineering
secondary_domains: [migrations, operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0023, DBKB-RDBE-0012]
related: [DBKB-RDBE-0016, DBKB-RDBE-0018]
aliases: [safe schema change]
search_keywords: [ddl, migration, lock, expand contract, rollback]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009, SRC-000038]
acceptance_criteria: [Precondition/postcondition/rollback workflow-t ad, Lock és dependency impactot követel]
---
# Safe DDL Changes

Safe DDL change előtt rögzítsd a preconditiont, dependency graphot, lock/rewrite kockázatot, data
backfillt, compatibilityt és rollback utat. Additive expand–contract deployment csökkentheti a
simultaneous old/new consumer problémát.

Staging rehearsal, representative size, timeout, observability és abort criterion kötelező. `DROP`,
rename, type narrowing és `NOT NULL` dirty data esetén külön destructive review kell. Rollback nem
mindig inverse DDL: adatvesztő művelethez backup vagy forward repair szükséges.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
