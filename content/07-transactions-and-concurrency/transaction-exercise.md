---
schema_version: 1
id: DBKB-TX-0025
title: Transaction Exercise
type: exercise
primary_domain: transactions-and-concurrency
secondary_domains: [practice]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: cross-vendor
prerequisites: [DBKB-TX-0003, DBKB-TX-0004, DBKB-TX-0006]
related: [DBKB-TX-0024]
aliases: [transaction lab]
search_keywords: [transaction exercise, rollback exercise, savepoint lab]
risk: safe
version_sensitive: false
review_cycle: 12m
research_packages: [RP-TX-0001]
source_ids: [SRC-000007, SRC-000014]
acceptance_criteria: [Rollback, savepoint és isolation kérdéseket reproducible SQLite feladattal gyakoroltat]
---
# Transaction Exercise

Hozz létre két account sort, indíts transactiont, módosíts egyenleget, majd mutasd be a `ROLLBACK` és `SAVEPOINT` hatását. Rögzítsd a statementeket, expected final state-et és a tényleges SQLite harness evidence-et.

Isolation kérdésnél különítsd el a lokális SQLite eredményt a PostgreSQL vagy más engine dokumentált behaviorétől; ne generalizálj execution nélkül.

## Források
- [IBM — ACID properties](https://www.ibm.com/think/topics/acid-database)
- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
