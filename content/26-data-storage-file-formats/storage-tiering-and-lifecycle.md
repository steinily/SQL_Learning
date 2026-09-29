---
schema_version: 1
id: DBKB-STOR-0013
title: Storage Tiering and Lifecycle
type: concept
primary_domain: data-storage
secondary_domains: [governance, cost]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [parquet, apache-orc, apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0012]
related: []
aliases: [data storage lifecycle]
search_keywords: [hot warm cold archive, retention, lifecycle, restore latency]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000073]
acceptance_criteria: [Tier choice, retention, retrieval and deletion trade-offs are explained]
---
# Storage Tiering and Lifecycle

Tiering hot/warm/cold/archive storage között cost, access latency, minimum retention, retrieval fee, durability, encryption és recovery requirement alapján dönt. Lifecycle expiry snapshot, legal hold, orphan file és catalog reference policy-val együtt kezelendő; olcsó tier nem automatikusan recoverable.

## Források
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
