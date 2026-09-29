---
schema_version: 1
id: DBKB-MY-0021
title: Group Replication
type: technology
primary_domain: mysql-mariadb
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql]
sql_dialects: [mysql]
scope: vendor-specific
prerequisites: [DBKB-MY-0020]
related: [DBKB-MY-0022]
aliases: [MySQL Group Replication]
search_keywords: [Group Replication, multi-primary, quorum, consistency]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046]
acceptance_criteria: [Group membership, certification, quorum, single/multi-primary és failure scopeját adja]
---
# Group Replication

MySQL Group Replication group membership, certification és quorum alapján koordinált replicationt ad. Single-primary/multi-primary mode, network partition, conflict és recovery behavior operational drillt igényel.

## Források
- [MySQL 8.4 — Group Replication](https://dev.mysql.com/doc/refman/8.4/en/group-replication.html)
