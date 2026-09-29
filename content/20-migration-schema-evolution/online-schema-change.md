---
schema_version: 1
id: DBKB-MIG-0007
title: Online Schema Change
type: technology
primary_domain: migration
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0006]
related: []
aliases: [online DDL]
search_keywords: [online DDL, low lock, instant alter, zero downtime]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Online/instant claims are scoped and evidence requirements are explicit]
---
# Online Schema Change

Online, in-place vagy instant jelző csak konkrét command, storage engine, version és workload mellett értelmezhető. Ne ígérj zero downtime-ot: ellenőrizd metadata lockot, brief commit lockot, replication, trigger/backfill behavior-t, cancellation-t és actual application latency-t.

## Források
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
- [Microsoft — Modify Columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/modify-columns-database-engine)
