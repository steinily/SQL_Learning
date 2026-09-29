---
schema_version: 1
id: DBKB-OPS-0006
title: Storage and Capacity Operations
type: technology
primary_domain: database-operations
secondary_domains: [capacity-planning]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0004]
related: []
aliases: [database capacity management]
search_keywords: [storage growth, capacity, disk pressure, tablespace]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Capacity signals, thresholds and response are described]
---
# Storage and Capacity Operations

Capacity management a data growth, free space, I/O headroom, log vagy WAL growth és backup footprint trendjeire épül. Threshold esetén előbb mérd a growth source-ot és a retention policy-t; storage expansion önmagában nem helyettesíti a root-cause elemzést.

## Források
- [PostgreSQL — Managing Disk Usage](https://www.postgresql.org/docs/current/diskusage.html)
