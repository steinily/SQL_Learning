---
schema_version: 1
id: DBKB-CAP-0050
title: Reference MySQL
type: reference
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
prerequisites: [DBKB-CAP-0049]
related: [DBKB-MY-0001]
aliases: [MySQL quick reference]
search_keywords: [MySQL reference, InnoDB, EXPLAIN, binlog, replication]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [MySQL navigation, InnoDB, query, replication and backup controls are summarized]
---
# Reference MySQL

Navigation: MySQL SQL; InnoDB transactions/locks; `EXPLAIN`; indexes; metadata locks; binlog/replication; backup/restore; users/privileges; performance schema.

Record server/engine/config version and validate online DDL, replication and backup behavior in the target environment. Syntax portability is limited by engine and release.

## Forrás
- [MySQL Documentation](https://dev.mysql.com/doc/)
