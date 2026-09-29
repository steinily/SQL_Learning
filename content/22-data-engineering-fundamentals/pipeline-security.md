---
schema_version: 1
id: DBKB-DE-0019
title: Pipeline Security
type: technology
primary_domain: data-engineering
secondary_domains: [security-privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-airflow, parquet]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DE-0018]
related: []
aliases: [data pipeline security]
search_keywords: [pipeline security, secret, encryption, access, data exposure]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000066, SRC-000067]
acceptance_criteria: [Identity, secrets, data access, logging and isolation controls are addressed]
---
# Pipeline Security

Pipeline security külön kezelje orchestration identity-t, worker identity-t, source/sink credentials-t, secret rotationt, network access-t, encryptiont, artifact permissions-t és sensitive data maskingot. Debug output, notebook, temporary file és failed task log is data exfiltration path lehet.

## Források
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
