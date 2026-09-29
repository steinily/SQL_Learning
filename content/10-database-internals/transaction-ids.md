---
schema_version: 1
id: DBKB-INT-0010
title: Transaction IDs
type: technology
primary_domain: database-internals
secondary_domains: [concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0009]
related: [DBKB-INT-0011]
aliases: [transaction ID wraparound]
search_keywords: [transaction ID, xid, wraparound, horizon]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Transaction ID age, wraparound és vacuum kapcsolatát írja le]
---
# Transaction IDs

Transaction ID age korlátozott reprezentáció miatt wraparound kockázatot hordozhat. A routine vacuum és monitoring tartja fenn a szükséges horizon-t; emergency anti-wraparound vacuum esetén a write availability veszélybe kerülhet.

## Források
- [PostgreSQL 18 — Preventing Transaction ID Wraparound Failures](https://www.postgresql.org/docs/18/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND)
