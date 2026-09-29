---
schema_version: 1
id: DBKB-CLOUD-0011
title: Cloud Data Migration
type: playbook
primary_domain: cloud-data-platforms
secondary_domains: [migration, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [aws-data-platform, google-bigquery, snowflake]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CLOUD-0010]
related: [DBKB-MIG-0001]
aliases: [cloud migration]
search_keywords: [cloud data migration, rehost, refactor, CDC, cutover, reconciliation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CLOUD-0001]
source_ids: [SRC-000098, SRC-000099, SRC-000100]
acceptance_criteria: [Inventory, landing, transformation, dual-run, cutover, rollback and cost validation are covered]
---
# Cloud Data Migration

Migration előtt inventoryzd a source schema, volume, classification, lineage, SLA, query és cost profile-t. Döntsd el workloadonként a rehost, replatform, refactor vagy retire irányt; target cloud service feature parityt ne feltételezz.

Snapshot/CDC/dual-run után compare count, checksum, business invariant, freshness, permission és cost. Cutoverhoz freeze/lag boundary, consumer communication, rollback, DNS/endpoint, IAM és decommission evidence kell.

## Források
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
