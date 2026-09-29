---
schema_version: 1
id: DBKB-MODL-0006
title: Denormalization
type: concept
primary_domain: data-modeling
secondary_domains: [performance, analytics]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0005, DBKB-FND-0016]
related: [DBKB-MODL-0016, DBKB-MODL-0023]
aliases: [redundant read model]
search_keywords: [denormalization, cache, materialization, consistency]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MODL-0001, RP-MODL-0003]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria: [Trade-offként mutatja be, Refresh és consistency contractot követel]
---
# Denormalization

Denormalization tudatosan tárol redundant vagy előre összesített adatot, hogy bizonyos read workload kevesebb join/compute művelettel szolgálható legyen. Minden duplicated facthez ownership, refresh, repair és reconciliation policy kell.

Tipikus forma summary table, materialized projection, cached label vagy read-optimized wide row. Transactionally maintained denormalization más garanciát ad, mint asynchronous refresh. „Kevesebb join gyorsabb” mérés nélkül nem bizonyított állítás.

Redundant storage növeli write amplificationt, migration complexityt és stale-data kockázatot. Előbb representative queryvel mérj, majd rögzíts invariánsokat és repair runbookot.

## Források

- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
