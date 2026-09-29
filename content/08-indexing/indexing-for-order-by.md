---
schema_version: 1
id: DBKB-IDX-0020
title: Indexing for ORDER BY
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
scope: vendor-specific
prerequisites: [DBKB-IDX-0003]
related: [DBKB-IDX-0005]
aliases: [ordered index scan]
search_keywords: [ORDER BY index, sort avoidance, index ordering]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [ORDER BY és index direction kapcsolatát írja le]
---
# Indexing for ORDER BY

Megfelelő index order esetén a planner elkerülheti a külön sort lépést. A direction, NULLS ordering, filter selectivity és LIMIT együtt döntik el, hogy az ordered scan valóban előnyös-e.

## Források
- [PostgreSQL 18 — Indexes and ORDER BY](https://www.postgresql.org/docs/18/indexes-ordering.html)
