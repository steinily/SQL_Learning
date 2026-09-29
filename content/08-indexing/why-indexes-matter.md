---
schema_version: 1
id: DBKB-IDX-0002
title: Why Indexes Matter
type: concept
primary_domain: indexing
secondary_domains: [performance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-IDX-0001]
related: [DBKB-IDX-0010, DBKB-IDX-0022]
aliases: [index benefit]
search_keywords: [index benefit, sequential scan, random access]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Benefit és write/storage trade-offot selectivityvel köti össze]
---
# Why Indexes Matter

Index akkor hasznos, ha a lekérdezés által keresett sorok és a teljes relation aránya, az ordering és a hozzáférési költség indokolja. A planner döntését `EXPLAIN` és aktuális statistics alapján ellenőrizd.

## Források
- [PostgreSQL 18 — Indexes](https://www.postgresql.org/docs/18/indexes.html)
