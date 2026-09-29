---
schema_version: 1
id: DBKB-MODL-0003
title: ER Modeling
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
prerequisites: [DBKB-MODL-0002]
related: [DBKB-MODL-0004, DBKB-MODL-0020]
aliases: [entity relationship model]
search_keywords: [entity, attribute, relationship, ERD, associative entity]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-MODL-0001]
source_ids: [SRC-000009]
acceptance_criteria:
  - Entity, attribute és relationship fogalmakat definiál.
  - M:N kapcsolat associative entity mappingját bemutatja.
---
# ER Modeling

Entity olyan domain object, amelynek saját identityje és lifecycle-ja van; attribute a state egy részlete; relationship entityk közötti üzleti kapcsolat. ER diagram a cardinality, optionality, ownership és identifier döntéseket review-olható formába teszi.

M:N kapcsolatot relational schema tipikusan associative relationship table-re bont. A relationship saját attributumai — például `quantity` vagy `effective_from` — ebben a table-ben kapnak helyet.

Ne emelj minden noun-t entityvé. Ha nincs stable identity, lifecycle és business behavior, lehet, hogy attribute vagy lookup value. Minden relationshipnél kérdezd meg: bizonyítható-e a cardinality és explicit-e a nullable kapcsolat jelentése.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
