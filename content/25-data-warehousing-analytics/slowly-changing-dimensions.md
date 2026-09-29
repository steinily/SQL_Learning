---
schema_version: 1
id: DBKB-WH-0005
title: Slowly Changing Dimensions
type: technology
primary_domain: data-warehouse
secondary_domains: [data-modeling]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0004]
related: []
aliases: [SCD]
search_keywords: [slowly changing dimension, type 1, type 2, effective date, current flag]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066]
acceptance_criteria: [SCD strategies, effective dates and late correction are explained]
---
# Slowly Changing Dimensions

SCD Type 1 overwrite, Type 2 historizál effective dates/version rows alapján; más type-ek külön trade-offot adnak. Business key match, current flag, time boundary, late correction, duplicate source update és fact join semantics legyen tesztelve.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
