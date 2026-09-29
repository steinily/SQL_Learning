---
schema_version: 1
id: DBKB-MODL-0023
title: Schema Evolution and Compatibility
type: concept
primary_domain: data-modeling
secondary_domains: [migrations, operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0019, DBKB-SQL-0022]
related: [DBKB-MODL-0010, DBKB-MODL-0024]
aliases: [schema migration compatibility]
search_keywords: [schema evolution, expand contract, backward compatible, migration]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria: [Breaking és additive change-t elkülönít, Expand-contract és rollback risket ad]
---
# Schema Evolution and Compatibility

Schema change akkor biztonságos, ha producer, consumer, migration és rollback contractja ismert. Additive
column gyakran backward-compatible, de `NOT NULL` default, type narrowing, rename/drop és key change
breaking lehet.

Expand-contract minta: új struktúra bevezetése, dual read/write vagy backfill, consumer migration,
validáció, majd régi út eltávolítása. Large table lock, index build, trigger és replication impact
külön analysis.

Migration idempotency, precondition, postcondition és recovery path kötelező. A source code módosítása
önmagában nem bizonyít schema compatibilityt.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
