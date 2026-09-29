---
schema_version: 1
id: DBKB-DE-0018
title: Data Engineering Observability
type: technology
primary_domain: data-engineering
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow, opentelemetry]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0017]
related: []
aliases: [pipeline observability]
search_keywords: [pipeline metrics, freshness, volume, lineage, task duration]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Pipeline health signals, freshness and lineage correlation are defined]
---
# Data Engineering Observability

Pipeline observability mérje run state, duration, input/output volume, freshness, lag, error/retry, partition skew, resource saturation és lineage. Orchestrator/task green mellett data quality vagy completeness failure lehet; independent assertions és downstream impact signal szükséges.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
