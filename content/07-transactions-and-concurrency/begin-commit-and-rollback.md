---
schema_version: 1
id: DBKB-TX-0003
title: BEGIN COMMIT and ROLLBACK
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [sql-fundamentals]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-TX-0002]
related: [DBKB-TX-0004, DBKB-SQL-0021]
aliases: [transaction commands]
search_keywords: [begin, commit, rollback, atomicity]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000007, SRC-000014]
acceptance_criteria: [Commit és rollback expected state-et futtatott példával bizonyít, Destructive opt-int követel]
---
# BEGIN COMMIT and ROLLBACK

`BEGIN` transaction boundaryt nyit, `COMMIT` az addigi módosításokat véglegessé teszi, `ROLLBACK`
elveti azokat. Driver-ek autocommit mode-ja külön figyelmet igényel: explicit boundary nélkül minden
statement önálló transaction lehet.

Módosítás előtt preview, affected-row assertion és postcondition legyen. A rollback csak database
transactionben résztvevő state-et állítja vissza; external side effectet nem.

A `SQL-TX-0003` SQLite-ban commitolt és rollbackelt account balance-t ellenőriz isolated in-memory
database-on.

## Források

- [IBM — ACID properties](https://www.ibm.com/docs/en/cics-tx/11.1.0?topic=processing-acid-properties-transactions)
- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
