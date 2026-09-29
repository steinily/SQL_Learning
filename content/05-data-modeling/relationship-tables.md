---
schema_version: 1
id: DBKB-MODL-0020
title: Relationship Tables
type: concept
primary_domain: data-modeling
secondary_domains: [relational-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0004, DBKB-MODL-0007]
related: [DBKB-ISQL-0016, DBKB-MODL-0011]
aliases: [junction table, associative table]
search_keywords: [many-to-many, junction, association, composite key]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009]
acceptance_criteria: [M:N mappingot és relationship attributumokat bemutat, Duplicate pair constraintet megad]
---
# Relationship Tables

Relationship table M:N associationt bont két 1:N foreign key-re. Composite primary key vagy equivalent
unique constraint tiltja ugyanazon pair nem kívánt duplikációját. Relationship saját attributumai,
például role, quantity vagy effective interval, itt tárolhatók.

Cascade és delete policy mindkét parentre külön döntés. Temporal vagy tenant scope esetén a pair key
része lehet a scope. Query grain: egy relationship row egy association instance, nem parent snapshot.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
