---
schema_version: 1
id: DBKB-MY-0018
title: Isolation and Locking
type: technology
primary_domain: mysql-mariadb
secondary_domains: [concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0017]
related: [DBKB-MY-0020]
aliases: [InnoDB isolation]
search_keywords: [MySQL isolation, InnoDB locking, deadlock, gap lock]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Isolation, record/gap lock, blocking és deadlock scopeját adja]
---
# Isolation and Locking

InnoDB isolation és row/gap locking visibility, blocking és deadlock behaviorét befolyásolja. Isolation setting, index access path, transaction duration és engine version alapján kell a concurrent claimet bizonyítani.

## Források
- [MySQL 8.4 — InnoDB Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html)
