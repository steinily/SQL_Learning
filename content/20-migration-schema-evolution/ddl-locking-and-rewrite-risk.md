---
schema_version: 1
id: DBKB-MIG-0006
title: DDL Locking and Rewrite Risk
type: technology
primary_domain: migration
secondary_domains: [concurrency, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0005]
related: []
aliases: [DDL lock risk]
search_keywords: [DDL lock, table rewrite, metadata lock, blocking]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Lock, rewrite, duration and cancellation risks are distinguished]
---
# DDL Locking and Rewrite Risk

DDL command lock mode-ja, table rewrite-ja, transaction duration-a és concurrent workloadra gyakorolt hatása engine/version/operation specific. Migration előtt target builden mérj representative data-val, állíts timeout/abort policy-t, és monitorozd a blockers, I/O és replication impactet.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
