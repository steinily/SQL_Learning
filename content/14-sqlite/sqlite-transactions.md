---
schema_version: 1
id: DBKB-SQ-0006
title: SQLite Transactions
type: concept
primary_domain: sqlite
secondary_domains: [concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-SQ-0002]
related: [DBKB-SQ-0007, DBKB-SQ-0008]
aliases: [BEGIN DEFERRED, IMMEDIATE, EXCLUSIVE]
search_keywords: [SQLite transaction, deferred, immediate, exclusive]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQ-0001]
source_ids: [SRC-000048]
acceptance_criteria: [Transaction type, atomicity, autocommit és writer contention scopeját adja]
---
# SQLite Transactions

SQLite `DEFERRED`, `IMMEDIATE` és `EXCLUSIVE` transaction modes eltérő lock acquisition timingot adnak. Atomicity erős, de concurrent writer behavior és busy handling application pattern függő.

## Források
- [SQLite — Transaction](https://www.sqlite.org/lang_transaction.html)
