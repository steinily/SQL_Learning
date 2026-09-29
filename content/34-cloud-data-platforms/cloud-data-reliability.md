---
schema_version: 1
id: DBKB-CLOUD-0009
title: Cloud Data Reliability
type: playbook
primary_domain: cloud-data-platforms
secondary_domains: [reliability, disaster-recovery]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0008]
related: [DBKB-DR-0001]
aliases: [cloud data SRE]
search_keywords: [cloud data reliability, SLO, RPO, RTO, backup, region failure]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [SLO, quota, backup, restore, failure and provider dependency controls are defined]
---
# Cloud Data Reliability

Data reliability SLO: availability, freshness, completeness, correctness, latency és recovery. Provider SLA ne legyen automatikusan workload SLO; quota exhaustion, regional outage, IAM failure, network/egress és service degradation külön failure mode.

Backup/restore, cross-region strategy, RPO/RTO, dependency inventory, incident communication és failback legyen gyakorolt. Managed service esetén is legyen exit/portability és degraded-mode terv, amelyet tényleges restore vagy game day evidence támaszt alá.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
