---
schema_version: 1
id: DBKB-TX-0001
title: Transactions and Concurrency Overview
type: overview
primary_domain: transactions-and-concurrency
secondary_domains: [operations, data-integrity]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0007, DBKB-MODL-0019]
related: [DBKB-TX-0002, DBKB-TX-0006, DBKB-TX-0017]
aliases: [transaction fundamentals]
search_keywords: [transaction, acid, isolation, lock, mvcc, retry]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000007, SRC-000014]
acceptance_criteria: [Lifecycle, ACID, isolation és retry fogalmakat összeköti, engine scope-ot explicitál]
---
# Transactions and Concurrency Overview

Transaction egy atomic state-change boundary: több statement együtt commitol vagy rollbackol. ACID
vocabulary atomicity, consistency, isolation és durability; konkrét guarantee az adott engine, isolation
és storage configuration függvénye.

Concurrency designnál rögzítsd a shared state-et, invariantokat, isolation contractot, lock/wait
behavior-t, deadlock/retry policyt és external side effect boundaryt. A database transaction nem teszi
automatikusan atomic-ká az emailt, queue publish-t vagy HTTP hívást.

Local fixture-ek SQLite-on csak a deklarált subsetet igazolják. PostgreSQL MVCC/isolation állítások
source-verifiedek, elérhető PostgreSQL multi-session runtime nélkül nem execution-verifiedek.

## Források

- [IBM — ACID properties](https://www.ibm.com/docs/en/cics-tx/11.1.0?topic=processing-acid-properties-transactions)
- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
