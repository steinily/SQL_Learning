---
schema_version: 1
id: DBKB-IDX-0015
title: Clustered Indexes
type: comparison
primary_domain: indexing
secondary_domains: [storage]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver]
sql_dialects: [postgresql, tsql]
scope: cross-vendor
prerequisites: [DBKB-IDX-0003]
related: [DBKB-IDX-0016]
aliases: [clustered storage order]
search_keywords: [clustered index, physical order, heap]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Clustered fogalmat PostgreSQL/SQL Server scope különbséggel mutatja]
---
# Clustered Indexes

A clustered index fogalma engine-specific: egyes rendszerek storage ordert kötnek indexhez, PostgreSQL-ben a `CLUSTER` művelet fizikai rendezést végez, amely később nem marad automatikusan karbantartva.

## Források
- [PostgreSQL 18 — CLUSTER](https://www.postgresql.org/docs/18/sql-cluster.html)
