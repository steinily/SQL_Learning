---
schema_version: 1
id: DBKB-CAP-0034
title: Warehouse Exercise
type: exercise
primary_domain: capstone
secondary_domains: [data-warehousing, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, google-bigquery, snowflake]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0033]
related: [DBKB-WH-0001]
aliases: [warehouse lab]
search_keywords: [warehouse exercise, incremental load, partition, freshness, cost]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000099, SRC-000100]
acceptance_criteria: [Learner builds incremental warehouse load, partition strategy, cost guard and reconciliation]
---
# Warehouse Exercise

Építs incremental fact loadot watermarktal és late-arriving handlinggel, majd tervezz partition/clustering, aggregate refresh, quality/freshness, query cost és backfill ellenőrzést.

Evidence: source/target count, checksum/invariant, query profile, bytes/scan vagy warehouse resource, freshness és rollback. Provider-specific execution outputot külön csatold.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Snowflake Documentation](https://docs.snowflake.com/)
