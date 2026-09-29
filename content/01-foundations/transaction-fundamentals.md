---
schema_version: 1
id: DBKB-FND-0025
title: Transaction Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [transactions, sql]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0003, DBKB-FND-0024]
related: [DBKB-FND-0026, DBKB-FND-0027]
aliases: [transaction block, commit, rollback]
search_keywords: [BEGIN, COMMIT, ROLLBACK, savepoint, boundary]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0001, RP-FND-0004]
source_ids: [SRC-000006, SRC-000014]
acceptance_criteria:
  - Meghatározza a transaction boundaryt és outcome-ot.
  - Bemutatja az autocommit, savepoint és error handling alapját.
  - Runnable commit/rollback példát kapcsol.
---
# Transaction Fundamentals

A **transaction** összetartozó database operationök egysége, amely `COMMIT` vagy `ROLLBACK`
outcome-mal zárul. A boundarynek a business invarianthez kell igazodnia: ami együtt helyes,
annak együtt kell commitolnia.

PostgreSQL 18-ban explicit block `BEGIN` és `COMMIT` között fut; `ROLLBACK` elveti a block
módosításait. Explicit block nélkül minden statement implicit transactionben fut. Client
library további transaction policyt alkalmazhat, ezért az autocommit feltételezését ellenőrizd.

## Lifecycle

1. Transaction indul, és isolation/access mode állapotot kap.
2. Statementek olvasnak vagy módosítanak; constraint check az engine szabályai szerint fut.
3. Error esetén a transaction abort state-be kerülhet.
4. `COMMIT` sikerrel teszi véglegessé a változásokat, vagy conflict/failure miatt hibázik.
5. `ROLLBACK` visszavonja a nem committed database módosításokat.

## Savepoint

Savepoint részleges rollback pont, nem független nested transaction. A külső transaction
rollbackje a savepoint előtt megtartott változásokat is elveti. Használd lokális error recoveryre,
de ne keverd external side-effect kompenzációval.

## Boundary anti-pattern

Hosszú user interaction közben nyitva tartott transaction lockot, snapshotot és resource-t
foglalhat. Túl kicsi boundary viszont partial business state-et enged. A megoldás gyakran rövid
database transaction plusz idempotent workflow state.

A `SQL-FND-0012` actual SQLite futásban commitált és rollbackelt update eredményét egyszerre
ellenőrzi.

## Források

- [PostgreSQL 18 — Transactions](https://www.postgresql.org/docs/18/tutorial-transactions.html)
- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
