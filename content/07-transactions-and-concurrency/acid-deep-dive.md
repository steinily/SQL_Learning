---
schema_version: 1
id: DBKB-TX-0005
title: ACID Deep Dive
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [foundations]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-TX-0001, DBKB-FND-0007]
related: [DBKB-TX-0006, DBKB-TX-0017]
aliases: [atomicity consistency isolation durability]
search_keywords: [acid, atomicity, consistency, isolation, durability]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000007, SRC-000014]
acceptance_criteria: [Négy ACID tulajdonságot és korlátait megmagyarázza, External side effect boundaryt ad]
---
# ACID Deep Dive

Atomicity: a transaction all-or-nothing database state change. Consistency: committed state satisfies
declared constraints/invariants. Isolation: concurrent transactions látható interactionja a chosen
level szerint korlátozott. Durability: commit után recovery esetén is megőrzött state a system contractja.

ACID nem azt jelenti, hogy minden business invariant automatikusan létezik, és nem teszi atomikussá a
database-en kívüli emailt, paymentet vagy message publish-t. Constraint, isolation, WAL/storage és
recovery configuration együtt ad tényleges guarantee-t.

## Források

- [IBM — ACID properties](https://www.ibm.com/docs/en/cics-tx/11.1.0?topic=processing-acid-properties-transactions)
- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
