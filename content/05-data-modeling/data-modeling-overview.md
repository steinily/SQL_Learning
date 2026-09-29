---
schema_version: 1
id: DBKB-MODL-0001
title: Data Modeling Overview
type: overview
primary_domain: data-modeling
secondary_domains: [foundations, relational-design]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0001, DBKB-FND-0019]
related: [DBKB-MODL-0002, DBKB-MODL-0005, DBKB-MODL-0017]
aliases: [database design]
search_keywords: [model, entity, relationship, grain, key, normalization]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-MODL-0001, RP-MODL-0002, RP-MODL-0003]
source_ids: [SRC-000009, SRC-000010, SRC-000013, SRC-000016]
acceptance_criteria:
  - Elkülöníti a conceptual logical és physical modelt.
  - A grain, identity, constraints és lifecycle fogalmakat összeköti.
---
# Data Modeling Overview

Data model a domain fontos dolgait, kapcsolatait, azonosítását, grainjét és integrity szabályait teszi explicit-té. A jó modell nem pusztán table-lista: megmutatja, mi egy sor jelentése, ki a felelős érte, milyen állapotokon megy át, és mely invariánsokat kell minden writernek betartania.

A conceptual model domain vocabularyt ad; a logical model relationöket, attribute-okat és relationshipeket rendez; a physical model engine, type, index, partition és storage döntéseket rögzít. A rétegek összekeverése korai optimalizálást és rejtett business szabályokat okoz.

Minden modeling döntést négy kérdéssel review-olj: mi a grain; mi a stable identity; mely értékek engedélyezettek; milyen history és ownership kell. A constraint a database-en belüli executable contract, de nem helyettesít governance-t vagy application authorizationt.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
