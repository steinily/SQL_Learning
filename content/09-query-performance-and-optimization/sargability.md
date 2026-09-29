---
schema_version: 1
id: DBKB-PERF-0015
title: Sargability
type: concept
primary_domain: query-performance
secondary_domains: [indexing]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-PERF-0007]
related: [DBKB-IDX-0008]
aliases: [search argument optimization]
search_keywords: [sargability, function on column, predicate rewrite]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Sargable és nem-sargable predicate példát ad plan evidence-szel]
---
# Sargability

Sargable predicate lehetővé teszi, hogy az access path közvetlenül a keresett értékre szűkítsen. Oszlopra alkalmazott function, implicit cast vagy leading wildcard ezt akadályozhatja; rewrite csak szemantikai equivalence bizonyítása után történjen.

## Források
- [PostgreSQL 18 — Indexes on Expressions](https://www.postgresql.org/docs/18/indexes-expressional.html)
