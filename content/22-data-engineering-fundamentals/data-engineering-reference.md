---
schema_version: 1
id: DBKB-DE-0025
title: Data Engineering Reference
type: reference
primary_domain: data-engineering
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0008, DBKB-DE-0018]
related: []
aliases: [data engineering checklist]
search_keywords: [data engineering reference, pipeline checklist, freshness, lineage]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067, SRC-000068]
acceptance_criteria: [Reference checklist covers contract, quality, operations and cost]
---
# Data Engineering Reference

Pipeline review checklist: source/target contract, schema evolution, lineage, partition/file layout, idempotency, retries, freshness, data quality, access/security, observability, cost, backfill, retention és runbook evidence. A checklist csak review aid; target platform execution és owner sign-off szükséges.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Apache Parquet Documentation](https://parquet.apache.org/docs/)
