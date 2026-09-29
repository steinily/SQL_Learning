---
schema_version: 1
id: DBKB-MODL-0015
title: Entity-Attribute-Value Modeling
type: comparison
primary_domain: data-modeling
secondary_domains: [data-quality, semi-structured-data]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0005, DBKB-FND-0012]
related: [DBKB-MODL-0016, DBKB-ASQL-0018]
aliases: [EAV]
search_keywords: [entity attribute value, sparse attributes, extensibility]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria: [EAV trade-offot és query/constraint kockázatot bemutat, JSON és typed-column alternatívát ad]
---
# Entity-Attribute-Value Modeling

EAV külön row-kban tárolja az entity, attribute name és value hármast. Ritka, user-defined vagy
gyorsan változó attribute készletnél rugalmas, de type, validation, uniqueness, indexing és query
shape nehézzé válik.

Ha az attribute üzletileg stabil és gyakran szűrt, typed column vagy normalized child table általában
jobb. Semi-structured JSON alternatíva lehet, de schema contract, path validation és index policy akkor
is szükséges. EAV nem távolítja el a data modelt; implicit modelt hoz létre metadata table-ekben és
application logicban.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
