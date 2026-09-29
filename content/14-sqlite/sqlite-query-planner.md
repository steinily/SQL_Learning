---
schema_version: 1
id: DBKB-SQ-0011
title: SQLite Query Planner
type: concept
primary_domain: sqlite
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-SQ-0010]
related: [DBKB-SQ-0005]
aliases: [SQLite query planner]
search_keywords: [SQLite query planner, EXPLAIN QUERY PLAN, cost-based choice]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQ-0001]
source_ids: [SRC-000048]
acceptance_criteria: [Planner choices and plan inspection are explained without invented output]
---
# SQLite Query Planner

SQLite selects query plans from available indexes and table access strategies. `EXPLAIN QUERY PLAN` is a diagnostic interface, but its output is version-sensitive; capture it from the target SQLite build and avoid treating a sample plan as universal execution evidence.

## Források
- [SQLite — The SQLite Query Planner](https://www.sqlite.org/queryplanner.html)
