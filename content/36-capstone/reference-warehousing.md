---
schema_version: 1
id: DBKB-CAP-0060
title: Reference Warehousing
type: reference
primary_domain: capstone
secondary_domains: [data-warehousing, performance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, google-bigquery, snowflake]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0059]
related: [DBKB-WH-0001]
aliases: [warehouse checklist]
search_keywords: [warehouse reference, fact, dimension, partition, incremental, cost]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000099, SRC-000100]
acceptance_criteria: [Warehouse model, loading, partition, quality, performance, cost and recovery checklist is provided]
---
# Reference Warehousing

Checklist: grain/fact/dimension; key/late data; watermark/incremental; partition/clustering; SCD; quality/reconciliation; query plan/scan; freshness; cost/quota; security; backup/restore; lineage; rollback.

Backfill és aggregate refresh legyen idempotent, bounded és post-validated; provider-specific scan/cost semanticset exact docs és execution output alapján kezeld.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
