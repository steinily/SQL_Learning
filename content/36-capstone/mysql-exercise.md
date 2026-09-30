---
schema_version: 1
id: DBKB-CAP-0030
title: MySQL Exercise
type: exercise
primary_domain: capstone
secondary_domains: [mysql, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mysql]
sql_dialects: [mysql]
scope: vendor-specific
prerequisites: [DBKB-CAP-0029]
related: [DBKB-MY-0001]
aliases: [MySQL lab]
search_keywords: [MySQL exercise, InnoDB, EXPLAIN, lock, replication]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner documents InnoDB plan, metadata lock, replication, backup and recovery checks]
---
# MySQL Exercise

MySQL/InnoDB labban reproduce-olj egy metadata lock és replica lag esetet, majd mérj `EXPLAIN`, transaction, backup és recovery behavior-t.

Rögzítsd engine/version/config, workload, commands, output, expected result, cleanup és rollback. Binlog/replication vagy online DDL claim csak actual execution és official version documentation mellett elfogadható.

## Forrás
- [MySQL Documentation](https://dev.mysql.com/doc/)
