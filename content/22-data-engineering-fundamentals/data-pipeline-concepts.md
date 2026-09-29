---
schema_version: 1
id: DBKB-DE-0002
title: Data Pipeline Concepts
type: concept
primary_domain: data-engineering
secondary_domains: [pipelines]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0001]
related: []
aliases: [data pipeline basics]
search_keywords: [source, sink, transform, dependency, watermark]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Source, transform, sink, dependency and state concepts are explained]
---
# Data Pipeline Concepts

Pipeline source-ból olvas, transformál, sink-be ír, és state/checkpoint alapján folytatható. Documentáld schema/contractot, orderinget, watermarkot, retryt, late data policy-t és ownershipet; a „pipeline succeeded” csak output validation után jelent helyes adatot.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
