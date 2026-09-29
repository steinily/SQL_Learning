---
schema_version: 1
id: DBKB-RDBE-0002
title: Physical Table Design
type: concept
primary_domain: relational-database-engineering
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0005, DBKB-MODL-0017]
related: [DBKB-RDBE-0003, DBKB-RDBE-0007]
aliases: [table physical design]
search_keywords: [table, column, type, row, storage, grain]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009, SRC-000010, SRC-000011, SRC-000038]
acceptance_criteria: [Grain type nullability és constraint döntéseket összekapcsolja, Table contractot ad]
---
# Physical Table Design

Physical table design a row grainből indul: minden columnnak legyen jelentése, type-ja, nullabilityje
és ownershipje. Válassz a domainnek megfelelő exact/temporal/character type-ot; a túl tág text és a
túl szűk numeric egyaránt későbbi hibát okozhat.

Explicit column list, stable naming, primary key, alternate uniqueness és foreign key legyen. Default
csak akkor helyes, ha a business meaning valóban implicit értéket enged. Generated vagy audit column
ne legyen client által szabadon írható.

Physical storage option és table partition engine-specific; performance claimhez mérés kell.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
