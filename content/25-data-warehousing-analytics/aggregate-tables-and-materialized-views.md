---
schema_version: 1
id: DBKB-WH-0013
title: Aggregate Tables and Materialized Views
type: technology
primary_domain: data-warehouse
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0012]
related: []
aliases: [precomputed aggregate]
search_keywords: [aggregate table, materialized view, refresh, invalidation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066, SRC-000073]
acceptance_criteria: [Precomputation, refresh, freshness and semantic consistency are defined]
---
# Aggregate Tables and Materialized Views

Aggregate table vagy materialized view read costot csökkenthet, de refresh, invalidation, freshness, late correction és semantic drift kockázatot ad. Measure definition, source grain, refresh window, failure/rebuild path és consumer fallback legyen dokumentálva.

## Források
- [Apache Spark — SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
