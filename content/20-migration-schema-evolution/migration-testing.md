---
schema_version: 1
id: DBKB-MIG-0013
title: Migration Testing
type: playbook
primary_domain: migration
secondary_domains: [testing-validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0012]
related: []
aliases: [migration verification]
search_keywords: [migration test, rehearsal, compatibility, data parity]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Rehearsal, compatibility, data parity and failure tests are specified]
---
# Migration Testing

Migration testingben syntax/metadata, existing data, new writes, old/new application versions, concurrency, rollback/roll-forward, performance és recovery path szerepeljen. Representative volume és target engine build nélkül a rehearsal eredménye csak korlátozott evidence.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [Microsoft — Modify Columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/modify-columns-database-engine)
