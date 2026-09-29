---
schema_version: 1
id: DBKB-TX-0002
title: Transaction Lifecycle
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
prerequisites: [DBKB-TX-0001]
related: [DBKB-TX-0003, DBKB-TX-0017]
aliases: [transaction state]
search_keywords: [begin, active, commit, rollback, aborted]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000007, SRC-000014]
acceptance_criteria: [Begin/active/commit/rollback lifecyclet leírja, Error utáni state-et és cleanupot kezeli]
---
# Transaction Lifecycle

Typical lifecycle: begin, statements, commit vagy rollback. Constraint/runtime error transactiont
aborted state-be vihet; explicit rollback vagy driver cleanup kell, mielőtt a connection új munkát kap.

Commit után a database state tartósan látható a contract szerinti többi sessionnek; rollback az
atomic boundaryn belüli state changeket elveti. External resources és client retry külön boundary.

Connection poolnél a transaction mindig visszaadott connection cleanupjával záruljon, különben a
következő request örökölt state-et vagy lockot láthat.

## Források

- [IBM — ACID properties](https://www.ibm.com/docs/en/cics-tx/11.1.0?topic=processing-acid-properties-transactions)
- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
