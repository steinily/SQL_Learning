---
schema_version: 1
id: DBKB-TX-0017
title: Transaction Boundaries
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
prerequisites: [DBKB-TX-0002, DBKB-TX-0009]
related: [DBKB-TX-0018, DBKB-TX-0022]
aliases: [unit of work, transaction scope]
search_keywords: [transaction boundary, unit of work, commit scope]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Boundary tervezési trade-offokat atomicity és lock duration szerint mutatja be]
---
# Transaction Boundaries

A transaction boundary jelzi, mely műveletek commitolnak vagy rollbackelnek együtt. Legyen elég széles az üzleti invariáns védelméhez, de elég rövid a lock duration és retry-költség korlátozásához.

Külső hálózati hívást általában ne tarts nyitott database transactionben; ha atomicity kell, tervezz outbox vagy kompenzáló folyamatot, és dokumentáld az eltérő failure modelt.

## Források

- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
