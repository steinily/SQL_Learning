---
schema_version: 1
id: DBKB-RDBE-0007
title: Index Overview
type: concept
primary_domain: relational-database-engineering
secondary_domains: [performance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0017, DBKB-SQL-0006]
related: [DBKB-RDBE-0002, DBKB-RDBE-0014]
aliases: [index fundamentals]
search_keywords: [index, lookup, write cost, selectivity, covering]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria: [Index benefit és write/storage costot összevet, Design decisiont plan és measurementhez köt]
---
# Index Overview

Index access structure, amely bizonyos predicate/order/workload shape-eket gyorsíthat, de minden
insert/update/delete írási költséget, storage-ot és maintenance-t ad. Index nem correctness substitute
és nem garantál használatot.

Design workflow: representative query, predicate/order/join shape, selectivity és cardinality,
candidate index, execution plan, write benchmark, majd production monitoring. Over-indexing lassít és
konfliktusos storage/maintenance costot hoz.

Index type, included/partial/expression syntax és concurrent build engine-specific. M06 csak alapozó;
deep B-tree és optimizer témák későbbi modulokban lesznek.

## Források

- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
