---
schema_version: 1
id: DBKB-MODL-0008
title: UUID Keys
type: technology
primary_domain: data-modeling
secondary_domains: [postgresql, distributed-systems]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0007]
related: [DBKB-MODL-0018, DBKB-MODL-0014]
aliases: [globally unique identifier]
search_keywords: [uuid, guid, key, distributed id, randomness]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-MODL-0002]
source_ids: [SRC-000009, SRC-000010]
acceptance_criteria: [UUID trade-offokat és privacy kockázatot bemutat, Business key helyett technikai identityként kezeli]
---
# UUID Keys

UUID technikai identifier, amely központi sequence coordination nélkül generálható. Ez hasznos
distributed writer-eknél és external API-kban, de nem business identity. A business uniquenesset
külön `UNIQUE` constraint védje.

Trade-off a nagyobb key/index footprint, random insertion miatti locality-kockázat, text/binary
representation, generation quality és operációs debugolhatóság. UUID kiszivárogtatása sem authorization;
a key unguessability nem access control.

Válassz engine-native type-ot, ha van; különben canonical formatot és validationt dokumentálj.
Generation version és collision policy legyen explicit. Migrationnél old/new key mapping és foreign
key rollout szükséges.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [PostgreSQL 18 — Numeric Types](https://www.postgresql.org/docs/18/datatype-numeric.html)
