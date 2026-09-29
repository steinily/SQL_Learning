---
schema_version: 1
id: DBKB-MIG-0008
title: Data Backfill
type: playbook
primary_domain: migration
secondary_domains: [data-quality, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0007]
related: []
aliases: [schema backfill]
search_keywords: [backfill, chunking, throttling, checkpoint, reconciliation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Chunking, checkpoint, throttling, idempotency and reconciliation are defined]
---
# Data Backfill

Backfill legyen chunkolt, resumable, idempotent és workload-aware; checkpoint, retry, dead-letter vagy exception path tartozzon hozzá. Mérd rows processed, lag, lock/I/O impact és reconciliation totals értékeket, és csak verified parity után tedd kötelezővé az új constraintet.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
