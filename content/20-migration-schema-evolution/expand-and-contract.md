---
schema_version: 1
id: DBKB-MIG-0004
title: Expand and Contract
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
prerequisites: [DBKB-MIG-0003]
related: []
aliases: [expand contract migration]
search_keywords: [expand contract, backward compatible schema, deprecation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Expand, migrate, switch and contract phases are explained]
---
# Expand and Contract

Expand phase-ben additiv schema vagy compatibility layer kerül be, migrate phase-ben az adat és consumers átállnak, switch után contract phase távolítja el a régi path-ot. Minden phase külön deploy és observability gate legyen; unused column drop előtt usage evidence szükséges.

## Források
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
- [Microsoft — Modify Columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/modify-columns-database-engine)
