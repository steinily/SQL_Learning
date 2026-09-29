---
schema_version: 1
id: DBKB-PG-0019
title: Foreign Data Wrappers
type: technology
primary_domain: postgresql
secondary_domains: [integration]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0014]
related: [DBKB-PG-0020]
aliases: [FDW, foreign table]
search_keywords: [foreign data wrapper, foreign server, postgres_fdw]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [FDW pushdown, transaction és credential boundaryt dokumentálja]
---
# Foreign Data Wrappers

FDW remote data source-ot foreign table-ként tesz elérhetővé. Pushdown, transaction semantics, remote failure, credential storage és network latency miatt local table equivalence nem feltételezhető.

## Források
- [PostgreSQL 18 — Foreign Data](https://www.postgresql.org/docs/18/ddl-foreign-data.html)
