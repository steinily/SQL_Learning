---
schema_version: 1
id: DBKB-CAP-0051
title: Reference SQLite
type: reference
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
prerequisites: [DBKB-CAP-0050]
related: [DBKB-SQ-0001]
aliases: [SQLite quick reference]
search_keywords: [SQLite reference, WAL, pragma, locking, backup, integrity]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [SQLite navigation, journaling, locking, integrity and backup controls are summarized]
---
# Reference SQLite

Navigation: SQLite SQL/DDL; `PRAGMA`; transactions; rollback/WAL journal; busy timeout; locking; integrity check; backup API/file boundary; indexes and query plan.

Record SQLite version/compile options/pragmas and connection lifecycle. Test concurrent access and restore before making durability or performance claims.

## Forrás
- [SQLite Documentation](https://www.sqlite.org/docs.html)
