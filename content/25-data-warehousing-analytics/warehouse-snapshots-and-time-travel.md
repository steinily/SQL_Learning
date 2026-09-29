---
schema_version: 1
id: DBKB-WH-0018
title: Warehouse Snapshots and Time Travel
type: technology
primary_domain: data-warehouse
secondary_domains: [reliability, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-iceberg]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-WH-0017]
related: []
aliases: [table snapshots time travel]
search_keywords: [snapshot, time travel, version, snapshot expiration, rollback]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-WH-0001]
source_ids: [SRC-000073]
acceptance_criteria: [Snapshot identity, retention, time travel and data lifecycle are explained]
---
# Warehouse Snapshots and Time Travel

Snapshot/table version immutable state point-in-time olvasást, auditot vagy rollback supportot adhat; retention expiry, catalog consistency, delete files, compaction és storage cost korlát. Time travel nem helyettesíti backup/DR-t, és feature supportot target engine/catalog párossal kell ellenőrizni.

## Források
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
