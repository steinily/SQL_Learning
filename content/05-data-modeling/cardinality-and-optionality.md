---
schema_version: 1
id: DBKB-MODL-0004
title: Cardinality and Optionality
type: concept
primary_domain: data-modeling
secondary_domains: [relational-design]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0003, DBKB-FND-0019]
related: [DBKB-SQL-0018, DBKB-MODL-0020]
aliases: [relationship cardinality]
search_keywords: [one-to-one, one-to-many, many-to-many, optionality, nullability]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-MODL-0001]
source_ids: [SRC-000009]
acceptance_criteria: [1:1 1:N és M:N kapcsolatokat elkülönít, Optionality és nullable foreign key kapcsolatát tisztázza]
---
# Cardinality and Optionality

Cardinality megmondja, egy entity instance hány másik instance-szal kapcsolódhat. 1:N esetben a many oldalon foreign key áll; M:N esetén relationship table szükséges. Optionality azt mondja meg, hogy a kapcsolat kötelező-e: `0..1`, `1..1`, `0..N` vagy `1..N`.

Nullable foreign key tipikusan optional parent kapcsolatot enged, de `NOT NULL` sem garantál minimum-one child kapcsolatot a parent oldalról. Ehhez workflow, deferred constraint vagy külön assertion lehet szükséges.

Foreign key referential integrityt véd, `UNIQUE` a „legfeljebb egy” oldalt. ON DELETE action lifecycle policy, nem technikai default. A `SQL-MODL-0004` fixture ezt a mappingot validálja.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
