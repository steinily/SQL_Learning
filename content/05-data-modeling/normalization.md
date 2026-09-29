---
schema_version: 1
id: DBKB-MODL-0005
title: Normalization
type: concept
primary_domain: data-modeling
secondary_domains: [relational-design, data-quality]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0003, DBKB-MODL-0004]
related: [DBKB-MODL-0006, DBKB-MODL-0017]
aliases: [normal forms]
search_keywords: [normalization, 1NF, 2NF, 3NF, update anomaly, dependency]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-MODL-0001]
source_ids: [SRC-000009]
acceptance_criteria: [Update insert és delete anomalykat bemutat, Functional dependency és grain kapcsolatát magyarázza]
---
# Normalization

Normalization a relationöket olyan formába rendezi, amely csökkenti a redundant tárolást és az update, insert, delete anomalykat. A gondolkodás alapja a grain és functional dependency: mely attribute-ok határoznak meg mely más attribute-okat.

Az 1NF atomic értékeket és ismétlődő csoportok elkerülését célozza; magasabb normal formák partial és transitive dependency-ket választanak szét. A pontos bizonyítás domain dependency-k ismeretét igényli.

Order headerben customer név ismétlése line-onként update anomalyt okoz; külön customer és order table FK-val egy helyen tartja a tényt. A normalization nem tilt minden denormalizációt: read model vagy cache explicit consistency policyval vállalható.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
