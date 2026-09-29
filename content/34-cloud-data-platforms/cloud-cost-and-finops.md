---
schema_version: 1
id: DBKB-CLOUD-0008
title: Cloud Cost and FinOps
type: playbook
primary_domain: cloud-data-platforms
secondary_domains: [governance, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0007]
related: [DBKB-OPS-0001]
aliases: [data platform FinOps]
search_keywords: [cloud cost, FinOps, query cost, egress, budget, chargeback]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Cost allocation, budgets, query controls, egress, optimization and unit economics are actionable]
---
# Cloud Cost and FinOps

Cost ownership legyen domain/project/tenant/workload szerint tagelt és chargeback/showback formában látható. Kövesd a storage, compute, scan, reservation/warehouse, network egress, backup és catalog költségét külön.

Budget alert, quota, max bytes/scanned data, auto-suspend, TTL, lifecycle tiering és approval gate csökkenti a meglepetést. Optimization csak latency/quality/SLO és data retention impact analysis után; benchmarkot tényleges workload outputtal támassz alá.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
