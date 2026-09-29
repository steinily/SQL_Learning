---
schema_version: 1
id: DBKB-MIG-0009
title: Dual Write and Dual Read
type: concept
primary_domain: migration
secondary_domains: [deployment]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0008]
related: []
aliases: [dual write migration]
search_keywords: [dual write, dual read, shadow read, consistency, cutover]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061]
acceptance_criteria: [Consistency, divergence detection and cutover risks are explained]
---
# Dual Write and Dual Read

Dual-write átmeneti compatibility technique, amely consistency, ordering, retry és partial failure kockázatot hoz. Divergence metric, reconciliation, idempotent write key, read cutover és old-path retirement explicit legyen; shadow read eredménye ne módosítsa a production state-et.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [Microsoft — Modify Columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/modify-columns-database-engine)
