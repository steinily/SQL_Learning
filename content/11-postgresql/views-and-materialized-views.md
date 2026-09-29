---
schema_version: 1
id: DBKB-PG-0018
title: Views and Materialized Views
type: concept
primary_domain: postgresql
secondary_domains: [schema-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0007]
related: [DBKB-PG-0020]
aliases: [view, materialized view]
search_keywords: [PostgreSQL view, materialized view, REFRESH MATERIALIZED VIEW]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [View virtuality és materialized refresh/consistency trade-offot adja]
---
# Views and Materialized Views

View query definitiont reprezentál, materialized view eredményt tárol és refresh policyt igényel. Freshness, refresh lock, indexes és consumer consistency legyen explicit; materialized output nem automatikusan current.

## Források
- [PostgreSQL 18 — Views](https://www.postgresql.org/docs/18/ddl-views.html)
