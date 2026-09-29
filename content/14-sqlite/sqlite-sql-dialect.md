---
schema_version: 1
id: DBKB-SQ-0005
title: SQLite SQL Dialect
type: reference
primary_domain: sqlite
secondary_domains: [sql]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-SQ-0001]
related: [DBKB-SQ-0004]
aliases: [SQLite syntax]
search_keywords: [SQLite SQL, grammar, pragmas, UPSERT]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQ-0001]
source_ids: [SRC-000048]
acceptance_criteria: [SQLite grammar, pragma, LIMIT, UPSERT és portability scopeját adja]
---
# SQLite SQL Dialect

SQLite SQL grammar saját `PRAGMA`, `LIMIT`, UPSERT és type affinity behaviorrel rendelkezik. Portable SQL claimhez dialect feature matrix és actual target engine execution szükséges.

## Források
- [SQLite — SQL Language](https://www.sqlite.org/lang.html)
