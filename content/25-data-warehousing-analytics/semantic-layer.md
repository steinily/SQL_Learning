---
schema_version: 1
id: DBKB-WH-0009
title: Semantic Layer
type: concept
primary_domain: data-warehouse
secondary_domains: [governance, analytics]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0008]
related: []
aliases: [analytics semantic model]
search_keywords: [semantic layer, metric definition, dimension, governed metric]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066]
acceptance_criteria: [Metric definitions, dimensions, grain and governance are described]
---
# Semantic Layer

Semantic layer közös business metric, dimension, filter, grain, join és access definitiont ad a BI/analytics fogyasztóknak. Metric definitionnek owner, calculation, time grain, null/unknown policy és test kell; ugyanazon „revenue” név eltérő grainnel veszélyes.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
