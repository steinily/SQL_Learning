---
schema_version: 1
id: DBKB-MIG-0022
title: Migration Exercise
type: exercise
primary_domain: migration
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0021]
related: []
aliases: [schema migration exercise]
search_keywords: [migration exercise, expand contract, backfill, rollback]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Migration Exercise

Tervezd meg egy additive column → backfill → dual-read → cutover → old-column removal migrationt. Készíts compatibility matrix-et, lock/rewrite rehearsal-t, parity assertiont, abort és roll-forward path-ot, observability dashboardot és evidence indexet; execution-verified csak tényleges futtatás után használható.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
