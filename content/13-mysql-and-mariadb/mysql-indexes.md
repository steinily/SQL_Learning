---
schema_version: 1
id: DBKB-MY-0014
title: MySQL Indexes
type: technology
primary_domain: mysql-mariadb
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0013]
related: [DBKB-MY-0016]
aliases: [MySQL index]
search_keywords: [MySQL index, BTREE, covering index, prefix index]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Index type, key order, prefix, covering és write cost trade-offot adja]
---
# MySQL Indexes

MySQL/MariaDB index behavior storage engine és version függő. InnoDB clustered primary key, secondary lookup, prefix index és covering design workload, cardinality, storage és write cost alapján értékelendő.

## Források
- [MySQL 8.4 — Optimization and Indexes](https://dev.mysql.com/doc/refman/8.4/en/optimization-indexes.html)
