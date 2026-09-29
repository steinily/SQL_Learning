---
schema_version: 1
id: DBKB-REC-0003
title: DML Recipes
type: cheatsheet
primary_domain: recipes
secondary_domains: [sql, data-quality]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0002]
related: [DBKB-DQ-0001]
aliases: [data change recipes]
search_keywords: [INSERT, UPDATE, DELETE, MERGE, DML, idempotent]
risk: destructive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [DML safety, predicate prechecks, idempotency, row counts and rollback are covered]
---
# DML Recipes

DML recipeben először `SELECT`-tel ellenőrizd a predicate-et és row countot; az `UPDATE`/`DELETE` ugyanazt a feltételt használja. Használj explicit transactiont, bounded batch-et, idempotency key-t és audit trailt, ahol támogatott.

Commit előtt verify-old affected rows, invariants, duplicate/null/foreign-key állapotot. Large destructive DML esetén backup, lock/replication impact, throttling és rollback/compensation kötelező; dry-run nélkül ne futtasd productionben.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
