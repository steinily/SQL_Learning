---
schema_version: 1
id: DBKB-WH-0004
title: Star and Snowflake Schemas
type: comparison
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
prerequisites: [DBKB-WH-0003]
related: []
aliases: [star schema snowflake schema]
search_keywords: [star schema, snowflake schema, normalization, join complexity]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066]
acceptance_criteria: [Schema trade-offs and workload implications are distinguished]
---
# Star and Snowflake Schemas

Star schema denormalized dimensions-szel egyszerűbb analytical join pathot adhat; snowflake schema normalized dimension hierarchiát és kevesebb redundanciát céloz, több join árán. Döntést query pattern, governance, update frequency, semantic reuse és engine optimization alapján hozd.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
