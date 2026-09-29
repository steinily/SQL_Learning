---
schema_version: 1
id: DBKB-TX-0004
title: Savepoints
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [sql-fundamentals]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-TX-0003]
related: [DBKB-TX-0002]
aliases: [nested transaction boundary]
search_keywords: [savepoint, rollback to, release]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Partial rollbackot és release lifecyclet megkülönbözteti, Fixture after-rollback state-et ellenőriz]
---
# Savepoints

Savepoint transactionön belüli partial rollback marker. `ROLLBACK TO SAVEPOINT` csak a marker utáni
state changeket veti el; a külső transaction tovább folytatható. `RELEASE SAVEPOINT` a markert eldobja,
nem commitálja a teljes transactiont.

Savepoint nem általános nested transaction és nem külső API side-effect rollback. Nagy számú savepoint
resource/lock overheadet okozhat; driver error handling és naming legyen explicit.

A `SQL-TX-0004` SQLite-ban egy invalid branch rollbackját, majd a transaction további commitját
ellenőrzi.

## Források

- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
