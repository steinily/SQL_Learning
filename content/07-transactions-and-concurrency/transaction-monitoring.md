---
schema_version: 1
id: DBKB-TX-0023
title: Transaction Monitoring
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0011, DBKB-TX-0022]
related: [DBKB-TX-0024]
aliases: [transaction observability, lock monitoring]
search_keywords: [transaction monitoring, lock metrics, transaction age]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Monitoring signaleket, dimensions és alert threshold caveat-et ad]
---
# Transaction Monitoring

Minimum signals: open transaction count, age, commit/rollback rate, lock wait duration, deadlock count, serialization failures és pool saturation. Dimenzióként service, database, role és deployment version kell.

Thresholdot baseline alapján állíts; a statikus érték nem univerzális. Incident során query text, pid/session és timestamp legyen korrelálható.

## Források
- [PostgreSQL 18 — Explicit Locking](https://www.postgresql.org/docs/18/explicit-locking.html)
