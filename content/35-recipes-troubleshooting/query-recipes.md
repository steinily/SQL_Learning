---
schema_version: 1
id: DBKB-REC-0004
title: Query Recipes
type: cheatsheet
primary_domain: recipes
secondary_domains: [sql, performance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0003]
related: [DBKB-PERF-0001]
aliases: [SQL query cookbook]
search_keywords: [SELECT, JOIN, pagination, explain, query recipe]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [Bounded query, parameterization, explain, pagination and result validation are covered]
---
# Query Recipes

Query recipe tartalmazzon explicit columns-t, stable orderinget, parameter bindingot, bounded predicate-et és expected cardinalityt. Paginationhez stable cursor vagy deterministic key kell; mutable data-n az offset könnyen skip/duplicate eredményt ad.

Performance claim előtt futtasd a dialect-specific explain/profile outputot representative statistics-szel. Validate-old null, duplicate, timezone, access-control és empty-result behavior-t; ad-hoc full scan productionben csak approved exceptionként fusson.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
