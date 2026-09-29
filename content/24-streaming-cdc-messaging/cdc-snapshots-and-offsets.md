---
schema_version: 1
id: DBKB-STREAM-0011
title: CDC Snapshots and Offsets
type: technology
primary_domain: streaming
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [debezium, apache-kafka, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0010]
related: []
aliases: [CDC snapshot offset]
search_keywords: [snapshot mode, log position, offset, restart, snapshot lock]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000070]
acceptance_criteria: [Snapshot consistency, offset handoff and restart behavior are covered]
---
# CDC Snapshots and Offsets

CDC snapshot existing state-et tölthet be, majd log positiontől folytat streamet; snapshot consistency, locking, chunking, offset persistence és restart mode kulcsfontosságú. Re-snapshot vagy offset reset adatduplikációt/gapet okozhat, ezért reconciliation és bounded replay szükséges.

## Források
- [Debezium Documentation](https://debezium.io/documentation/)
