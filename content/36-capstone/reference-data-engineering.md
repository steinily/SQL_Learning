---
schema_version: 1
id: DBKB-CAP-0057
title: Reference Data Engineering
type: reference
primary_domain: capstone
secondary_domains: [data-engineering, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0056]
related: [DBKB-DE-0001]
aliases: [data engineering checklist]
search_keywords: [data engineering reference, pipeline, batch, watermark, quality, lineage]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Pipeline, data quality, lineage, idempotency and recovery controls are summarized]
---
# Reference Data Engineering

Pipeline checklist: source contract; watermark/checkpoint; schema validation; idempotency; batch/stream semantics; quality/quarantine; lineage; observability; retry/DLQ; backfill/replay; reconciliation; owner/SLO; rollback.

Process completion csak source/output count, quality, freshness, lineage és business invariant post-check után állítható.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
