---
schema_version: 1
id: DBKB-TX-0010
title: Lock Modes
type: technology
primary_domain: transactions-and-concurrency
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0009]
related: [DBKB-TX-0011, DBKB-TX-0012]
aliases: [table lock mode, row-level lock mode]
search_keywords: [PostgreSQL lock mode, FOR UPDATE, lock compatibility]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Table és row-level lock mode példákat vendor scope-ban sorol]
---
# Lock Modes

PostgreSQL külön table-level és row-level lock módokat dokumentál. A `SELECT ... FOR UPDATE` például érintett sorokat zárolhat, de a teljes compatibility-táblát és a lock durationt mindig az adott statement és transaction boundary alapján kell értelmezni.

Lock mode neveket ne használd más engine-re változtatás nélkül; a terminológia és a compatibility matrix vendor-specific.

## Források

- [PostgreSQL 18 — Explicit Locking](https://www.postgresql.org/docs/18/explicit-locking.html)
