---
schema_version: 1
id: DBKB-MIG-0015
title: Cross-Engine Migration
type: comparison
primary_domain: migration
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0014]
related: []
aliases: [database platform migration]
search_keywords: [cross-engine migration, dialect, type mapping, compatibility]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Dialect, type, transaction, indexing and operational differences are identified]
---
# Cross-Engine Migration

Cross-engine migration nem csak DDL translation: type/null semantics, collations, identity/sequence, transaction isolation, locking, indexes, functions, extensions, backup, observability és operational tooling is eltérhet. Compatibility matrix, representative data és dual-run evidence nélkül a parity feltételezés nem bizonyított.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [Microsoft — Modify Columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/modify-columns-database-engine)
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
