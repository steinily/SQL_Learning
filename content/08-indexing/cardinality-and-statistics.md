---
schema_version: 1
id: DBKB-IDX-0011
title: Cardinality and Statistics
type: concept
primary_domain: indexing
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0010]
related: [DBKB-IDX-0018]
aliases: [planner statistics, column statistics]
search_keywords: [cardinality, statistics, ANALYZE, selectivity estimate]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Cardinality estimate és statistics szerepét plan validationnel írja le]
---
# Cardinality and Statistics

A planner cardinality estimate azt becsüli, hány row felel meg a feltételnek. PostgreSQL-ben az `ANALYZE` által gyűjtött statistics és a data distribution befolyásolja az index-versus-sequential scan döntést.

## Források
- [PostgreSQL 18 — Planner Statistics](https://www.postgresql.org/docs/18/planner-stats.html)
