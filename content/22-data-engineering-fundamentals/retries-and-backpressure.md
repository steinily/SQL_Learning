---
schema_version: 1
id: DBKB-DE-0015
title: Retries and Backpressure
type: concept
primary_domain: data-engineering
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0014]
related: []
aliases: [pipeline retry backpressure]
search_keywords: [retry, backpressure, queue, timeout, exponential backoff]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Retry classification, backoff, poison data and backpressure are explained]
---
# Retries and Backpressure

Retry csak transient és idempotens műveletre alkalmazható; permanent schema/data errort quarantine vagy fail path-ra kell küldeni. Exponential backoff, max attempts, timeout, queue depth és downstream capacity alapján backpressure-t érvényesíts, különben retry storm keletkezik.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
