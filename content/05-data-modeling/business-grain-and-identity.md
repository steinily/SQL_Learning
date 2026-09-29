---
schema_version: 1
id: DBKB-MODL-0017
title: Business Grain and Identity
type: concept
primary_domain: data-modeling
secondary_domains: [analytics, data-quality]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0007, DBKB-SQL-0014]
related: [DBKB-MODL-0018, DBKB-MODL-0019]
aliases: [row grain]
search_keywords: [grain, identity, business key, fact grain, duplicate]
risk: caution
version_sensitive: false
review_cycle: 12m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria: [Grain egy mondatos definícióját és key mappingját megadja, Duplicate és aggregation következményt bemutat]
---
# Business Grain and Identity

Grain egy row egyértelmű jelentése: például „egy order egy line-ja” vagy „egy customer egy napi
snapshotja”. Ha egy table több grain-t kever, join és aggregate eredmény bizonytalanná válik.

Identity azt mondja meg, mikor ugyanaz az entity vagy event. A surrogate technical key mellett
business uniqueness constraint kell, ha a domain tiltja a duplikációt. Fact grain, measurement unit,
time precision és source system is része a contractnak.

Model review első kérdése: „Mit jelent pontosan egy sor?” Második: „Mely attribute-ok lehetnek benne
egyszer?” A válasz vezeti a PK, UNIQUE, FK és aggregation design-t.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
