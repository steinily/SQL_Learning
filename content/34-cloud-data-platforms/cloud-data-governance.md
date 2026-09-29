---
schema_version: 1
id: DBKB-CLOUD-0005
title: Cloud Data Governance
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
prerequisites: [DBKB-CLOUD-0004]
related: [DBKB-DARCH-0010]
aliases: [cloud data governance]
search_keywords: [cloud catalog, policy tag, row access, masking, lineage, ownership]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Catalog, ownership, classification, access policy, lineage and retention controls are covered]
---
# Cloud Data Governance

Cloud governance rétegei: resource/account boundary, dataset/table ownership, classification, IAM/policy tag, row/column controls, lineage, quality, retention/legal hold és audit. A provider catalog nem helyettesíti a domain steward decision rights-ot.

Cross-account/project/share esetén dokumentáld a trust boundary-t, consumer approvalt, egress és revocation path-ot. Policy change előtt impact analysis, canary és rollback kell; generated metadata csak ténylegesen futó integration után tekinthető frissnek.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
