---
schema_version: 1
id: DBKB-IDX-0021
title: Indexing for Joins
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
scope: cross-vendor
prerequisites: [DBKB-IDX-0019]
related: [DBKB-IDX-0017]
aliases: [join key index]
search_keywords: [join index, nested loop, hash join]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Join index választást plan-alapú módszerrel írja le]
---
# Indexing for Joins

Join key index különösen nested-loop planban lehet hasznos, de hash vagy merge join esetén más költségmodell érvényes. Mindkét oldali cardinalityt és a join selectivityt együtt vizsgáld.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
