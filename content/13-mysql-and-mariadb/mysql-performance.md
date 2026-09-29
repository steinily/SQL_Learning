---
schema_version: 1
id: DBKB-MY-0027
title: MySQL Performance
type: playbook
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
prerequisites: [DBKB-MY-0016, DBKB-MY-0026]
related: [DBKB-MY-0028]
aliases: [MySQL tuning]
search_keywords: [MySQL performance, optimizer tuning, buffer pool, slow query]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Baseline, EXPLAIN, indexes, InnoDB, waits és workload tuning workflowet adja]
---
# MySQL Performance

MySQL/MariaDB tuning workflow: representative workload, `EXPLAIN`, slow log/Performance Schema, cardinality/index, InnoDB buffer/log, locks és replication signal; one change, after measurement, rollback. Fork/version scope mindig explicit.

## Források
- [MySQL 8.4 — Optimization](https://dev.mysql.com/doc/refman/8.4/en/optimization.html)
