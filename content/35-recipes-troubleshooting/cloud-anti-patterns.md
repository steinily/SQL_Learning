---
schema_version: 1
id: DBKB-REC-0048
title: Cloud Anti-Patterns
type: error
primary_domain: recipes
secondary_domains: [cloud-data-platforms, security]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0047]
related: [DBKB-CLOUD-0016]
aliases: [cloud mistakes]
search_keywords: [public bucket, broad IAM, egress surprise, quota, lock-in]
risk: security-sensitive
version_sensitive: true
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Cloud security, cost, reliability and portability anti-patterns are covered]
---
# Cloud Anti-Patterns

Anti-pattern public data endpoint, shared admin identity, untagged spend, no quota/budget, uncontrolled egress, region/residency mismatch, provider feature parity assumption és restore/exit drill hiánya.

Detectáld IAM/config scan, billing/resource tags, cost anomaly, quota alerts, residency audit és restore test alapján. Corrective action legyen scoped, reversible és provider/version evidence-re épített; emergency broad access expiry nélkül tilos.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
