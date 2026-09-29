---
schema_version: 1
id: DBKB-PERF-0009
title: Nested Loop Joins
type: technology
primary_domain: query-performance
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0004]
related: [DBKB-PERF-0012]
aliases: [nested loop plan]
search_keywords: [nested loop join, inner scan, join cost]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Nested loop outer/inner szerepét és scale kockázatát leírja]
---
# Nested Loop Joins

Nested loop az outer input minden sorához lefuttatja az inner hozzáférést. Kis outer set és jó inner index esetén hatékony, rossz cardinality estimate mellett viszont ismételt nagy scan költséget okozhat.

## Források
- [PostgreSQL 18 — Nested Loop](https://www.postgresql.org/docs/18/using-explain.html)
