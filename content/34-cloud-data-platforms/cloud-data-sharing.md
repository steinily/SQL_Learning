---
schema_version: 1
id: DBKB-CLOUD-0012
title: Cloud Data Sharing
type: technology
primary_domain: cloud-data-platforms
secondary_domains: [governance, security]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0011]
related: [DBKB-DARCH-0009]
aliases: [data share]
search_keywords: [cloud data sharing, cross-account, marketplace, secure view, revocation]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Share boundary, consumer authorization, masking, lifecycle, cost and revocation are defined]
---
# Cloud Data Sharing

Cloud sharing előtt jelöld a provider/consumer account-project boundary-t, data classificationt, row/column maskinget, purpose, retentiont, network/egress és billing ownershipot. Shared view/clone/marketplace interface-hez contract, owner és support path kell.

Access grant legyen least privilege, time-bounded és revocable; auditáld a consumer queryt és exportot. Producer schema change csak impact analysis, consumer notice és compatibility test után menjen át.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
