---
schema_version: 1
id: DBKB-MY-0020
title: Replication
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
prerequisites: [DBKB-MY-0019]
related: [DBKB-MY-0021]
aliases: [source/replica replication]
search_keywords: [MySQL replication, replica lag, GTID, source replica]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Source/replica, GTID, lag, failover és conflict scopeját adja]
---
# Replication

MySQL/MariaDB source/replica replication binary log eventsot továbbít, GTID és position alapján követve. IO/SQL/apply lag, filtering, DDL drift és failover readiness külön metrics és drill alapján értékelendő.

## Források
- [MySQL 8.4 — Replication](https://dev.mysql.com/doc/refman/8.4/en/replication.html)
