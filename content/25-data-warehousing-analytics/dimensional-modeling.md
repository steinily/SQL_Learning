---
schema_version: 1
id: DBKB-WH-0002
title: Dimensional Modeling
type: concept
primary_domain: data-warehouse
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0001]
related: []
aliases: [dimensional warehouse modeling]
search_keywords: [dimensional model, grain, fact, dimension, conformed dimension]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066]
acceptance_criteria: [Grain, facts, dimensions and conformance are explained]
---
# Dimensional Modeling

Dimensional modeling előtt rögzítsd a fact grain-t, business process-t, dimensions-t, measures-t és conformed dimensions-t. A grain ambiguity duplicate aggregationot okoz; model review-ban source lineage, late-arriving dimension és history policy is legyen.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
