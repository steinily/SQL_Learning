---
schema_version: 1
id: DBKB-MODL-0018
title: Natural and Surrogate Keys
type: comparison
primary_domain: data-modeling
secondary_domains: [relational-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0007, DBKB-MODL-0017]
related: [DBKB-MODL-0008]
aliases: [business key versus technical key]
search_keywords: [natural key, surrogate key, alternate key, immutability]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009]
acceptance_criteria: [Stabilitás, external exposure és migration trade-offot összevet, Mindkét uniqueness contractot kezeli]
---
# Natural and Surrogate Keys

Natural key domain-derived identity, például country code vagy external account number. Surrogate key
technikai identity, amelynek nincs domain jelentése. Natural key olvasható, de változhat, összetett
lehet és privacy exposure-t hordozhat; surrogate stabil FK graphot ad, de önmagában nem tilt business
duplikációt.

Gyakori modell a surrogate primary key és natural/alternate `UNIQUE` key együtt. A key választásnál
vizsgáld az external integrationt, merge/migrationt, tenant scope-ot és historical identityt.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
