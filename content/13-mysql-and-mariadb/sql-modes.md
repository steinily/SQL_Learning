---
schema_version: 1
id: DBKB-MY-0006
title: SQL Modes
type: technology
primary_domain: mysql-mariadb
secondary_domains: [compatibility]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0003]
related: [DBKB-MY-0007]
aliases: [sql_mode]
search_keywords: [sql_mode, strict mode, ANSI mode, compatibility]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [SQL mode result, strictness, migration és session/global scopeját adja]
---
# SQL Modes

MySQL `sql_mode` és MariaDB mode beállítások invalid input, implicit conversion, grouping és legacy syntax behaviorét módosíthatják. Migration és test environment ugyanazt a mode-ot használja, különben false compatibility confidence keletkezik.

## Források
- [MySQL 8.4 — Server SQL Modes](https://dev.mysql.com/doc/refman/8.4/en/sql-mode.html)
