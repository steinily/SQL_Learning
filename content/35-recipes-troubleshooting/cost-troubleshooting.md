---
schema_version: 1
id: DBKB-REC-0038
title: Cost Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [finops, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [google-bigquery, snowflake, aws-data-platform]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0037]
related: [DBKB-CLOUD-0008]
aliases: [data platform cost incident]
search_keywords: [unexpected cost, bytes scanned, egress, warehouse, budget]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Cost attribution, query/resource evidence, containment and optimization validation are covered]
---
# Cost Troubleshooting

Bontsd a cost spike-et provider/account/project, resource, tenant, query/job, storage, egress, backup és time window szerint. Capture-old query text/fingerprint, bytes scanned, warehouse/slot/concurrency, lifecycle és tags; ne csak számlát nézz.

Containment lehet quota, max scan, auto-suspend, workload throttle vagy export freeze. Optimization után verify-old latency, freshness, correctness és cost per unit; provider pricing/feature changes legyen linked és timestampelt.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
