---
schema_version: 1
id: DBKB-MY-0016
title: Optimizer and EXPLAIN
type: concept
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
related: [DBKB-MY-0027]
aliases: [MySQL query plan]
search_keywords: [MySQL EXPLAIN, optimizer, access type, cost]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [EXPLAIN output, estimates, access path és version caveat-et adja]
---
# Optimizer and EXPLAIN

MySQL/MariaDB optimizer cost és statistics alapján access pathot, join ordert és index használatot választ. `EXPLAIN` output estimated evidence; actual runtime, rows és I/O mérés külön szükséges.

## Források
- [MySQL 8.4 — EXPLAIN Statement](https://dev.mysql.com/doc/refman/8.4/en/explain.html)
