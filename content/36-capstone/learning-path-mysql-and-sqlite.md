---
schema_version: 1
id: DBKB-CAP-0073
title: Learning Path MySQL and SQLite
type: learning-path
primary_domain: capstone
secondary_domains: [mysql, sqlite]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mysql, sqlite]
sql_dialects: [mysql, sqlite]
scope: vendor-specific
prerequisites: [DBKB-CAP-0072]
related: [DBKB-CAP-0030, DBKB-CAP-0031]
aliases: [MySQL SQLite path]
search_keywords: [MySQL learning path, SQLite learning path, InnoDB, WAL, locking]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Ordered MySQL/SQLite path with engine-specific modeling, locking, backup and migration milestones]
---
# Learning Path MySQL and SQLite

Sorrend: SQL/modeling → MySQL InnoDB/query/replication/backup → SQLite file/WAL/locking/integrity → vendor exercises → case studies/reference.

Exit criteria: engine/version distinction, connection/lock diagnosis, safe migration, backup/restore and actual integrity evidence.

## Források
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
