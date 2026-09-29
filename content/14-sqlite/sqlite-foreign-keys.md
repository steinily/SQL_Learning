---
schema_version: 1
id: DBKB-SQ-0009
title: SQLite Foreign Keys
type: technology
primary_domain: sqlite
secondary_domains: [data-integrity]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-SQ-0005]
related: [DBKB-SQ-0010]
aliases: [SQLite referential integrity]
search_keywords: [SQLite foreign keys, PRAGMA foreign_keys, referential integrity]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQ-0001]
source_ids: [SRC-000048]
acceptance_criteria: [Foreign key enforcement configuration and constraints are explained]
---
# SQLite Foreign Keys

SQLite foreign key constraints are subject to runtime enforcement configuration. Applications should enable and verify `PRAGMA foreign_keys` on each connection, then test parent and child operations against the intended schema; declaring a constraint alone is not execution evidence.

## Források
- [SQLite — Foreign Key Support](https://www.sqlite.org/foreignkeys.html)
