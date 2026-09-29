---
schema_version: 1
id: DBKB-IDX-0018
title: Multi-Column Statistics
type: technology
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
prerequisites: [DBKB-IDX-0011]
related: [DBKB-IDX-0005]
aliases: [extended statistics]
search_keywords: [multivariate statistics, dependencies, ndistinct]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Extended statistics célját és korlátait dokumentálja]
---
# Multi-Column Statistics

Extended statistics több oszlop közötti dependency vagy distinct-count kapcsolatot írhat le, amely javíthatja a cardinality estimate-et. Nem helyettesíti az indexet, és hatása csak friss statistics után értékelhető.

## Források
- [PostgreSQL 18 — Extended Statistics](https://www.postgresql.org/docs/18/planner-stats.html#PLANNER-STATS-EXTENDED)
