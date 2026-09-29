---
schema_version: 1
id: DBKB-DE-0022
title: Pipeline Troubleshooting
type: troubleshooting
primary_domain: data-engineering
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0021]
related: []
aliases: [pipeline failure diagnosis]
search_keywords: [pipeline failure, stuck task, skew, schema error, retry storm]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Failure classification, evidence preservation and safe remediation are described]
---
# Pipeline Troubleshooting

Pipeline failuret source/schema, code, data, dependency, resource/skew, scheduler, permissions vagy infrastructure kategóriába sorold. Preserve-eld run ID-t, code/schema versiont, partition/input range-et és logs/metrics-et; blind retry helyett idempotency és partial output state alapján dönts.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
