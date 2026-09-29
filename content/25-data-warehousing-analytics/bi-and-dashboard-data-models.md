---
schema_version: 1
id: DBKB-WH-0014
title: BI and Dashboard Data Models
type: playbook
primary_domain: data-warehouse
secondary_domains: [analytics, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0013]
related: []
aliases: [BI serving model]
search_keywords: [BI model, dashboard, semantic metric, extract, freshness]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066, SRC-000068]
acceptance_criteria: [BI grain, metric ownership, freshness and access are defined]
---
# BI and Dashboard Data Models

BI model dashboard-grain, dimensions, measures, filters, drill path, freshness, row-level access és extract/cache behavior alapján készüljön. Dashboard totals-t reconcile-old warehouse semantic layerhez; visual correctness nem bizonyítja underlying data completeness vagy security correctness-ét.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
