---
schema_version: 1
id: DBKB-MIG-0020
title: Legacy Schema Modernization
type: case-study
primary_domain: migration
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0019]
related: []
aliases: [legacy database modernization]
search_keywords: [legacy schema, modernization, strangler, compatibility layer]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Case-study pattern is generic, evidence-based and non-fictional]
---
# Legacy Schema Modernization

Ez a case-study minta nem production esetet állít, hanem egy legacy schema modernization tervét mutatja: inventory → contract map → expand → backfill → dual path → cutover → contract. Minden fázisnál decision evidence, compatibility és exit criteria kell; konkrét vendor result csak futtatás után adható.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
- [Microsoft — Modify Columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/modify-columns-database-engine)
