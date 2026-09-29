---
schema_version: 1
id: DBKB-MODL-0002
title: Conceptual Logical and Physical Modeling
type: concept
primary_domain: data-modeling
secondary_domains: [relational-design]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0001]
related: [DBKB-MODL-0003, DBKB-MODL-0007]
aliases: [modeling layers]
search_keywords: [conceptual model, logical model, physical model, mapping]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-MODL-0001]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria:
  - Három modeling szintet különít el.
  - Mapping és loss-of-meaning kockázatot bemutat.
---
# Conceptual Logical and Physical Modeling

Conceptual model a domain entity és relationship vocabularyja technológiai részletek nélkül. Logical model ebből key-eket, attribute-okat, cardinalityt és integrity szabályokat vezet le. Physical model engine-specific objecteket, data type-okat, indexeket, partitiont és deployment korlátokat ad hozzá.

Egy logical entity physical representationje több table is lehet, például history és current state szétválasztásával. Fordítva több conceptual fogalom egy physical table-be kerülhet, ha a grain és ownership explicit marad. A mappingot dokumentáld, különben a physical schema lesz az egyetlen, gyakran félreérthető domain source.

OLTP workloadnál transaction boundary, constraint és write correctness; analytical workloadnál grain, scan shape és history hozzáférés befolyásolhat denormalizációt. Ezek trade-offok, nem univerzális szabályok.

## Források

- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
