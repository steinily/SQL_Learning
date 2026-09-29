---
schema_version: 1
id: DBKB-CLOUD-0010
title: Cloud Data Observability
type: technology
primary_domain: cloud-data-platforms
secondary_domains: [observability, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0009]
related: [DBKB-OBS-0001]
aliases: [cloud data monitoring]
search_keywords: [cloud data metrics, freshness, query latency, quota, cost observability]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Platform, workload, data quality, cost and security signals with runbook ownership are covered]
---
# Cloud Data Observability

Observability rétegei: provider/platform health, pipeline/job state, data freshness/completeness/schema, query latency/error/scan, quota/capacity, cost és IAM/security audit. Correláld a dataset identityt run, query, resource és incident timeline-mal.

Alerthez owner, threshold, duration, dedup/suppression, escalation és runbook kell. Provider metric önmagában nem bizonyít business correctnesset; domain-level quality és reconciliation signal is szükséges.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
