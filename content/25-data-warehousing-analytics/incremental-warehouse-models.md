---
schema_version: 1
id: DBKB-WH-0017
title: Incremental Warehouse Models
type: playbook
primary_domain: data-warehouse
secondary_domains: [data-engineering]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-spark, apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-WH-0016]
related: []
aliases: [incremental analytical model]
search_keywords: [incremental model, watermark, merge, late data, backfill]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000066, SRC-000073]
acceptance_criteria: [Incremental boundary, merge, late data and rebuild path are defined]
---
# Incremental Warehouse Models

Incremental model source watermark/partition alapján csak változott adatot dolgoz fel, de late update/delete, backfill, duplicate és correction policy explicit kell. Merge key, checkpoint, reconciliation, full rebuild és failure recovery path nélkül incremental load silent gapet hagyhat.

## Források
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
