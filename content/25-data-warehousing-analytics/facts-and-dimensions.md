---
schema_version: 1
id: DBKB-WH-0003
title: Facts and Dimensions
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
prerequisites: [DBKB-WH-0002]
related: []
aliases: [fact dimension design]
search_keywords: [fact table, dimension table, additive measure, grain]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066]
acceptance_criteria: [Fact grain, measure additivity, dimensions and keys are covered]
---
# Facts and Dimensions

Fact table a declared grain-en event vagy periodic snapshot metrics-ét tárolja; dimension descriptive contextet és historyt ad. Measures additive/semi-additive/non-additive jellegét, null/unknown member policy-t, key mappinget és late data behavior-t explicit módon dokumentáld.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
