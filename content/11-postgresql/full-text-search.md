---
schema_version: 1
id: DBKB-PG-0013
title: Full Text Search
type: technology
primary_domain: postgresql
secondary_domains: [search]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0008]
related: [DBKB-PG-0014]
aliases: [tsvector, tsquery]
search_keywords: [full text search, tsvector, tsquery, text search configuration]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [tsvector/tsquery, configuration és indexelés alapjait adja]
---
# Full Text Search

PostgreSQL full-text search `tsvector` dokumentum reprezentációt, `tsquery` keresési feltételt és language configurationt használ. Dictionary, stemming, ranking és GIN/GiST index behavior domain-specific; relevancia baseline-t mérd.

## Források
- [PostgreSQL 18 — Full Text Search](https://www.postgresql.org/docs/18/textsearch.html)
