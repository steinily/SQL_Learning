---
schema_version: 1
id: DBKB-CAP-0066
title: Reference Cloud
type: reference
primary_domain: capstone
secondary_domains: [cloud-data-platforms, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0065]
related: [DBKB-CLOUD-0001]
aliases: [cloud data checklist]
search_keywords: [cloud reference, IAM, region, cost, quota, restore, exit]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Cloud architecture, security, cost, reliability and portability checklist is provided]
---
# Reference Cloud

Checklist: region/residency; storage/compute; IAM/network/encryption; catalog/lineage; quality/freshness; quota/SLO; cost/egress; backup/restore; sharing/revocation; incident; provider exit.

Managed service feature, SLA, quota and pricing exact account/region/release contexttal értelmezendő.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
