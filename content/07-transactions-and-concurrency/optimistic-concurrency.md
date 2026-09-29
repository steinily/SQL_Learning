---
schema_version: 1
id: DBKB-TX-0015
title: Optimistic Concurrency
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [application-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-TX-0008]
related: [DBKB-TX-0016, DBKB-TX-0020]
aliases: [compare and swap, version column]
search_keywords: [optimistic concurrency, version column, conditional update]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Version predicate és conflict handling mintát ad, execution claim nélkül]
---
# Optimistic Concurrency

Optimistic concurrencynél az alkalmazás feltételezi, hogy ritka az ütközés, ezért conditional write-tal ellenőriz: `UPDATE ... WHERE id = ? AND version = ?`. Affected-row count jelzi, hogy a várt verzió még érvényes-e.

Conflict esetén explicit döntés kell: újraolvasás és merge, user-visible conflict vagy abort. Retry csak idempotens és bounded műveletnél biztonságos.

## Források

- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
