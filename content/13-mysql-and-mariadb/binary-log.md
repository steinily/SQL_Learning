---
schema_version: 1
id: DBKB-MY-0019
title: Binary Log
type: technology
primary_domain: mysql-mariadb
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0017]
related: [DBKB-MY-0020, DBKB-MY-0022]
aliases: [binlog]
search_keywords: [MySQL binary log, binlog format, row based replication]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Statement/row/mixed format, retention, recovery és replication roleját adja]
---
# Binary Log

Binary log changeset recovery és replication célra rögzít. Statement, row és mixed format külön determinism, size, privacy és replay semantics-et ad; retention és purge policy operationally critical.

## Források
- [MySQL 8.4 — Binary Log](https://dev.mysql.com/doc/refman/8.4/en/binary-log.html)
