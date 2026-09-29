---
schema_version: 1
id: DBKB-CLOUD-0013
title: Cloud Data Troubleshooting
type: troubleshooting
primary_domain: cloud-data-platforms
secondary_domains: [operations, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0012]
related: [DBKB-OPS-0001]
aliases: [cloud data incident runbook]
search_keywords: [cloud quota, query timeout, access denied, stale data, egress]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Quota, IAM, network, query, freshness and cost symptoms map to safe remediation]
---
# Cloud Data Troubleshooting

**Access denied:** azonosítsd principal, resource, policy inheritance, condition és region boundary-t; ne adj broad admin grantot workaroundként. **Quota/timeout:** ellenőrizd workload, reservation/warehouse, bytes scanned, concurrency és provider limitet, majd throttle-olj vagy izolálj.

**Stale/missing data:** trace-eld ingest/run watermark, catalog update, partition filter és downstream cache állapotot. **Unexpected cost:** bontsd resource/tenant/query/egress/retention szerint; változtatás előtt mentsd a cost evidence-et és rollbacket.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
