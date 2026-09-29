---
schema_version: 1
id: DBKB-MY-0015
title: Partitioning
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
prerequisites: [DBKB-MY-0014]
related: [DBKB-MY-0016]
aliases: [table partitioning]
search_keywords: [MySQL partitioning, partition pruning, range partition]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Partition method, pruning, key limitations és maintenance trade-offot adja]
---
# Partitioning

MySQL/MariaDB partitioning range, list, hash vagy key strategy szerint oszthat relationt. Partition pruning csak predicate alignment esetén segít; unique key, foreign key és engine limitation fork/version szerint ellenőrzendő.

## Források
- [MySQL 8.4 — Partitioning](https://dev.mysql.com/doc/refman/8.4/en/partitioning.html)
