---
schema_version: 1
id: DBKB-DE-0021
title: Data Engineering Testing
type: playbook
primary_domain: data-engineering
secondary_domains: [testing-validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0019]
related: []
aliases: [pipeline tests]
search_keywords: [pipeline test, fixture, schema assertion, data quality]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Unit, integration, data quality, contract and replay tests are covered]
---
# Data Engineering Testing

Pipeline testingben transform unit, schema/contract, fixture integration, data quality, replay/idempotency, performance, failure és end-to-end tests különítsd el. Expected row count és schema assertion mellett semantic reconciliation és late/duplicate event scenario is szükséges.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
