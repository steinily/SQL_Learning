---
schema_version: 1
id: DBKB-DE-0001
title: Data Engineering Fundamentals Overview
type: overview
primary_domain: data-engineering
secondary_domains: [pipelines, architecture]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0001]
related: []
aliases: [data engineering overview]
search_keywords: [data engineering, pipeline, processing, storage, orchestration]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Data engineering scope and operational concerns are defined]
---
# Data Engineering Fundamentals Overview

Data engineering a data source-ok ingestion, transformation, storage, serving és quality/observability útját tervezi és üzemelteti. A pipeline correctness, freshness, idempotency, lineage, security és cost együtt kezelendő; tool choice nem helyettesíti a data contractot.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
