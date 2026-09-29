---
schema_version: 1
id: DBKB-DE-0007
title: Idempotent Data Pipelines
type: concept
primary_domain: data-engineering
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0005, DBKB-DE-0006]
related: []
aliases: [replay-safe pipeline]
search_keywords: [idempotency, replay, deduplication, checkpoint, exactly once]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Replay, deduplication, checkpoint and side-effect safety are defined]
---
# Idempotent Data Pipelines

Idempotent pipeline ugyanazon inputot ismételve ugyanazt a verified state-et állítja elő, vagy explicit dedup/reconciliation mechanizmust használ. Stable event key, checkpoint, deterministic transform, atomic commit és side-effect isolation kell; retry önmagában nem exactly-once guarantee.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
