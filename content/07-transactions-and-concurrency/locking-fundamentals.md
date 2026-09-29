---
schema_version: 1
id: DBKB-TX-0009
title: Locking Fundamentals
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [concurrency]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0006]
related: [DBKB-TX-0010, DBKB-TX-0011]
aliases: [database lock, row lock]
search_keywords: [locking, row lock, lock wait]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Lock célját, hatókörét és wait behaviorét megkülönbözteti]
---
# Locking Fundamentals

A lock a konkurens műveletek ütközését kontrolláló adatbázis-eszköz. Elemzéskor különítsd el a lockolt objektumot, a lock módját, a birtokló tranzakciót és a várakozó tranzakciót.

Lock wait önmagában nem deadlock: deadlock esetén ciklikus függőség áll fenn, amelyet az engine megszakít. A pontos lock compatibility és monitoring nézet engine- és verziófüggő.

## Források

- [PostgreSQL 18 — Explicit Locking](https://www.postgresql.org/docs/18/explicit-locking.html)
