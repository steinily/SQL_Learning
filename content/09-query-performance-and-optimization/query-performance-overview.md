---
schema_version: 1
id: DBKB-PERF-0001
title: Query Performance Overview
type: overview
primary_domain: query-performance
secondary_domains: [optimization]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0023]
related: [DBKB-PERF-0002, DBKB-PERF-0023]
aliases: [query tuning]
search_keywords: [query performance, optimization, execution plan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Evidence-based query performance workflowet összefoglalja]
---
# Query Performance Overview

Query tuning sorrendje: reprodukálható workload, aktuális execution plan, cardinality és resource evidence, célzott változtatás, majd újramérés. A gyorsabbnak tűnő terv production bizonyíték nélkül nem tekinthető javulásnak.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
