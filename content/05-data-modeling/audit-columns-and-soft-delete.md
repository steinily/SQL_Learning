---
schema_version: 1
id: DBKB-MODL-0010
title: Audit Columns and Soft Delete
type: concept
primary_domain: data-modeling
secondary_domains: [operations, compliance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0007, DBKB-SQL-0021]
related: [DBKB-MODL-0011, DBKB-MODL-0023]
aliases: [created_at updated_at deleted_at]
search_keywords: [audit, soft delete, deleted_at, actor, retention]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MODL-0002, RP-MODL-0003]
source_ids: [SRC-000009, SRC-000013]
acceptance_criteria: [Audit columns és event history különbségét leírja, Soft delete visibility és retention policyt követel]
---
# Audit Columns and Soft Delete

`created_at`, `updated_at`, actor és source metadata hasznos current-row audit, de nem teljes változás
történet. History table, temporal event vagy CDC szükséges, ha minden transitiont és old value-t
meg kell őrizni.

Soft delete (`deleted_at`, state) megőrzi a row-t, de minden read querynek visibility predicate kell.
Unique key-eknél active-only uniqueness, restore collision és foreign key lifecycle explicit döntés.
Soft delete nem azonos retention, legal hold vagy erasure compliance-szel.

Timestamp timezone, clock source, actor trust, update trigger és backfill behavior legyen dokumentálva.
Audit oszlopot client inputként vakon elfogadni manipulálható.

## Források

- [PostgreSQL 18 — Date/Time Types](https://www.postgresql.org/docs/18/datatype-datetime.html)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
