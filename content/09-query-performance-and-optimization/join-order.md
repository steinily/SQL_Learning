---
schema_version: 1
id: DBKB-PERF-0012
title: Join Order
type: concept
primary_domain: query-performance
secondary_domains: [optimization]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0009, DBKB-PERF-0010, DBKB-PERF-0011]
related: [DBKB-PERF-0013]
aliases: [join tree]
search_keywords: [join order, join tree, cardinality]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Join order cardinality és intermediate result alapján értelmezhető]
---
# Join Order

Join order meghatározza az intermediate resultok méretét és a következő join inputját. Rossz estimate miatt a planner rossz join tree-t választhat; diagnózisnál estimated/actual rows minden szinten szükséges.

## Források
- [PostgreSQL 18 — Query Planning](https://www.postgresql.org/docs/18/explicit-joins.html)
