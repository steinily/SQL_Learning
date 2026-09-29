---
schema_version: 1
id: DBKB-MY-0022
title: Backup and Restore
type: playbook
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
prerequisites: [DBKB-MY-0019]
related: [DBKB-MY-0023]
aliases: [mysqldump, physical backup]
search_keywords: [MySQL backup, mysqldump, MySQL Enterprise Backup, restore test]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Logical/physical backup, binlog retention és restore verification lépéseit adja]
---
# Backup and Restore

Logical dump és physical backup eltérő consistency, speed, version és recovery scope-ot ad. Backup success nem restore proof; restore test, binlog availability, checksum és measured RTO szükséges.

## Források
- [MySQL 8.4 — Backup and Recovery](https://dev.mysql.com/doc/refman/8.4/en/backup-and-recovery.html)
