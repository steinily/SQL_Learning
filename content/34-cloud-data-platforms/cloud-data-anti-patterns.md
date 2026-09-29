---
schema_version: 1
id: DBKB-CLOUD-0016
title: Cloud Data Anti-Patterns
type: error
primary_domain: cloud-data-platforms
secondary_domains: [architecture, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0015]
related: [DBKB-DARCH-0016]
aliases: [cloud data mistakes]
search_keywords: [cloud anti-pattern, lift and shift, public bucket, uncontrolled cost, lock-in]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Common cloud data anti-patterns include detection and remediation]
---
# Cloud Data Anti-Patterns

Kerüld az unrestricted public data access-t, shared admin identityt, untagged resource-ot, uncontrolled cross-region egresset, query budget guard nélküli warehouse-t és backup restore drill nélküli „high availability”-t.

További anti-pattern a lift-and-shift workload fit/cost analysis nélkül, provider feature parity feltételezése, catalog/lineage nélküli lake, broad cross-account share és lock-in exit plan hiánya. Minden kivételhez owner, expiry, risk acceptance és remediation kell.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
