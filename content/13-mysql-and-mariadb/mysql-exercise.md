---
schema_version: 1
id: DBKB-MY-0029
title: MySQL Exercise
type: exercise
primary_domain: mysql-mariadb
secondary_domains: [practice]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0016, DBKB-MY-0022]
related: [DBKB-MY-0030]
aliases: [MySQL operations lab]
search_keywords: [MySQL exercise, EXPLAIN lab, backup restore lab]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [EXPLAIN, transaction, backup/restore és replication evidence feladatot adja]
---
# MySQL Exercise

Staging labban rögzíts SQL mode-ot és versiont, készíts EXPLAIN baseline-t, hajts végre kontrollált transactiont, ellenőrizd binlog/replication állapotot és végezz restore tesztet. Minden result engine/fork/version scope-hoz kötött.

## Források
- [MySQL 8.4 — Backup and Recovery](https://dev.mysql.com/doc/refman/8.4/en/backup-and-recovery.html)
