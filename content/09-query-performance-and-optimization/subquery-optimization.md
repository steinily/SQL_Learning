---
schema_version: 1
id: DBKB-PERF-0017
title: Subquery Optimization
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
prerequisites: [DBKB-PERF-0004]
related: [DBKB-PERF-0015]
aliases: [subquery decorrelation]
search_keywords: [subquery, correlated subquery, semi join]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Correlated és uncorrelated subquery plan trade-offot ír le]
---
# Subquery Optimization

Uncorrelated subquery gyakran önálló vagy join-szerű node-dá alakítható; correlated subquery outer soronként ismétlődhet. A rewrite csak azonos NULL és duplicate szemantikával tekinthető biztonságosnak.

## Források
- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
