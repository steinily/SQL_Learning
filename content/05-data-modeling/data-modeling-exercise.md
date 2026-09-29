---
schema_version: 1
id: DBKB-MODL-0025
title: Data Modeling Exercise
type: exercise
primary_domain: data-modeling
secondary_domains: [relational-design, data-quality]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [portable-sql, sqlite]
scope: portable-sql
prerequisites: [DBKB-MODL-0005, DBKB-MODL-0017, DBKB-MODL-0019]
related: [DBKB-MODL-0024]
aliases: [modeling practice]
search_keywords: [exercise, order model, grain, normalization, constraints]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009]
acceptance_criteria: [Feladatot, expected invariants és validation queryket ad]
---
# Data Modeling Exercise

Tervezd meg egy order workflow logical modeljét. Kötelező entity: customer, order, order line és
product. Írd le minden table grainjét, primary/alternate key-jét, cardinalityját, nullable columnjait,
állapotait és history policyját.

Acceptance criteria: nincs repeated product list; line quantity pozitív; order customer nélkül nem
létezhet; ugyanazon orderben line number unique; product price és order line amount jelentése explicit;
tenant vagy ownership scope rögzített.

Validation: invalid FK, duplicate key, zero quantity és orphan line negatív teszt; egy happy-path
fixture expected row counttal. A megoldás ne a syntax szépségét, hanem a grain és invariants bizonyítását
értékelje.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
