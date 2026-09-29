---
schema_version: 1
id: DBKB-DE-0024
title: Data Pipeline Exercise
type: exercise
primary_domain: data-engineering
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0023]
related: []
aliases: [data pipeline exercise]
search_keywords: [pipeline exercise, backfill, replay, data quality, runbook]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067, SRC-000068]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Data Pipeline Exercise

Építs batch pipeline-t Parquet inputból Spark transformationnel és Airflow orchestrationnel, majd szimulálj schema driftet, duplicate inputot és backfillt. Rögzíts lineage, quality assertions, retries, resource telemetry és reconciliation outputot; execution-verified csak valódi futtatás után használható.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
