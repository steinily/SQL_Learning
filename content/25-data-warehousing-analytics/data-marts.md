---
schema_version: 1
id: DBKB-WH-0010
title: Data Marts
type: technology
primary_domain: data-warehouse
secondary_domains: [architecture]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet, apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0009]
related: []
aliases: [subject area data mart]
search_keywords: [data mart, subject area, serving layer, conformed dimension]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066, SRC-000073]
acceptance_criteria: [Mart scope, conformance, refresh and ownership are defined]
---
# Data Marts

Data mart egy subject area vagy consumer céljára optimalizált serving layer. Mart scope, conformed dimension, refresh/freshness, semantic ownership, source lineage és deprecation policy legyen explicit, különben duplicated metric logic és divergent truth alakul ki.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
