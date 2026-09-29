---
schema_version: 1
id: DBKB-PERF-0029
title: Query Hints
type: comparison
primary_domain: query-performance
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver]
sql_dialects: [postgresql, tsql]
scope: cross-vendor
prerequisites: [DBKB-PERF-0022]
related: [DBKB-PERF-0030]
aliases: [optimizer hint]
search_keywords: [query hint, optimizer hint, forced plan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Hint használat trade-offját és vendor scopeját korlátozza]
---
# Query Hints

Optimizer hint vagy forced plan egy konkrét tervet preferálhat, de elfedheti a statistics vagy data-shape gyökerét, és verzióváltásnál törékeny lehet. Csak dokumentált ownerrel, expiryvel és rollbackkel alkalmazd.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
