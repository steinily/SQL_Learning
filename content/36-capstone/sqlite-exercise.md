---
schema_version: 1
id: DBKB-CAP-0031
title: SQLite Exercise
type: exercise
primary_domain: capstone
secondary_domains: [sqlite, embedded-database]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-CAP-0030]
related: [DBKB-SQ-0001]
aliases: [SQLite lab]
search_keywords: [SQLite exercise, WAL, locking, integrity, backup]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner tests SQLite locking, WAL, integrity, backup and schema migration]
---
# SQLite Exercise

Készíts concurrent reader/writer SQLite labot journal és WAL mode-ban, majd mérj busy/timeout, integrity check, backup/restore és schema migration behavior-t.

Rögzítsd SQLite version, pragmas, connection lifecycle, commands és actual outputot. Fájlkópia csak tested consistency boundary mellett tekinthető backupnak.

## Forrás
- [SQLite Documentation](https://www.sqlite.org/docs.html)
