---
schema_version: 1
id: DBKB-MODL-0007
title: Key Strategies
type: concept
primary_domain: data-modeling
secondary_domains: [relational-design, data-integrity]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0004, DBKB-FND-0010]
related: [DBKB-MODL-0008, DBKB-MODL-0018]
aliases: [primary key strategy]
search_keywords: [primary key, candidate key, natural key, surrogate key, unique]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-MODL-0001]
source_ids: [SRC-000009, SRC-000010]
acceptance_criteria: [Candidate primary alternate és foreign key fogalmakat elkülönít, Identity és mutable business attribute kockázatát kezeli]
---
# Key Strategies

Candidate key minden olyan minimal attribute-set, amely a row-t domain szerint egyedivé teszi. A primary key a választott identifier; alternate key `UNIQUE` constraintként maradhat. Foreign key a kapcsolódó entity key-jére hivatkozik.

Natural key business jelentést hordozhat, de változhat, hiányozhat, privacy-sensitive vagy összetett lehet. Surrogate key stabil technikai identity, de nem helyettesíti a business uniqueness constraintet. Gyakori helyes modell mindkettőt tartja.

Rögzítsd a generationt, nullabilityt, scope-ot, immutabilityt, external exposuret és migration behavior-t. A key type storage és index trade-off, nem önálló domain model.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
