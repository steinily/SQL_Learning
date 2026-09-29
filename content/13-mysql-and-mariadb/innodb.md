---
schema_version: 1
id: DBKB-MY-0013
title: InnoDB
type: technology
primary_domain: mysql-mariadb
secondary_domains: [storage]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql]
sql_dialects: [mysql]
scope: vendor-specific
prerequisites: [DBKB-MY-0002]
related: [DBKB-MY-0014, DBKB-MY-0018]
aliases: [InnoDB storage engine]
search_keywords: [InnoDB, clustered index, buffer pool, redo log]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046]
acceptance_criteria: [InnoDB clustered storage, buffer pool, redo/undo és transaction scopeját adja]
---
# InnoDB

InnoDB transactional storage engine clustered primary key, buffer pool, redo/undo log, MVCC és foreign key supportot ad. Table/index design és operational tuning InnoDB-specific; más engine behavior nem következtethető.

## Források
- [MySQL 8.4 — InnoDB Storage Engine](https://dev.mysql.com/doc/refman/8.4/en/innodb-storage-engine.html)
