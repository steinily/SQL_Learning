---
schema_version: 1
id: DBKB-DE-0004
title: ETL and ELT
type: comparison
primary_domain: data-engineering
secondary_domains: [architecture]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0002]
related: []
aliases: [ETL ELT patterns]
search_keywords: [ETL, ELT, transform, staging, warehouse]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066]
acceptance_criteria: [ETL/ELT placement and trade-offs are scoped to workload]
---
# ETL and ELT

ETL a target load előtt transformál, ELT pedig raw/staging load után target engine-ben vagy processing platformon. Döntést a compute, data sensitivity, replay, schema evolution, cost és consumer contract alapján hozd, ne általános teljesítményállításból.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
