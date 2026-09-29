---
schema_version: 1
id: DBKB-FND-0005
title: Database Models
type: concept
primary_domain: foundations
secondary_domains: [data-modeling, architecture]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: []
scope: general
prerequisites: [DBKB-FND-0002, DBKB-FND-0003]
related: [DBKB-FND-0006, DBKB-FND-0009, DBKB-FND-0032, DBKB-FND-0033]
aliases: [data model, database model]
search_keywords: [relational, hierarchical, network, document, key-value, graph]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0002]
source_ids: [SRC-000002, SRC-000003]
acceptance_criteria:
  - Elmagyarázza a model, logical structure és access pattern kapcsolatát.
  - Összehasonlítja a fő model family-ket túlzó product állítás nélkül.
  - A relational model canonical részleteire hivatkozik.
---
# Database Models

A **database model** meghatározza, milyen logikai elemekből áll az adat, hogyan kapcsolódnak,
és milyen műveletekkel érhetők el. Nem azonos a fizikai file formattal vagy egy konkrét
producttal: egy product több modellt is támogathat, ugyanaz a modell pedig több storage
mechanizmussal megvalósítható.

## Fő model family-k

- **Relational:** relation/table, tuple/row, attribute/column és deklarált key/constraint.
  Erőssége a formális műveleti alap és a composable declarative query. Részletei a
  [Relational Model Fundamentals](relational-model-fundamentals.md) dokumentumban vannak.
- **Hierarchical:** parent–child fa mentén szervezi az adatot. Természetes egyetlen ownership
  hierarchy esetén, de többirányú kapcsolatot nehezebb lehet kifejezni.
- **Network:** rekordok között több navigálható kapcsolatot enged; az access path a használó
  program számára hangsúlyos lehet.
- **Document:** önálló document aggregate-eket kezel, gyakran JSON-szerű representationnel.
  Az aggregate boundary és a query/update pattern döntő.
- **Key-value:** key alapján ér el opaque vagy részben értelmezett value-t. Egyszerű lookuphoz
  illeszkedik, összetett cross-key queryhez további structure kellhet.
- **Wide-column:** partition és clustering key köré szervezett, sparse row jellegű modellek.
- **Graph:** vertex és edge elsődleges elem; multi-hop traversal és relationship property
  központi.
- **Time-series/search/vector:** egy specializált access pattern és representation köré
  optimalizált modellek; gyakran más modellekkel együtt használatosak.

## Modelválasztás

Kiindulópont az access pattern és invariant:

- Milyen egységben írunk és olvasunk?
- Milyen kapcsolatot kell database-szinten védeni?
- Kell-e ad hoc query vagy előre ismert lookup elég?
- Milyen consistency és transaction boundary szükséges?
- Hogyan változik a schema és hogyan történik migration?
- Mi a partition key, és milyen query lépi át a partition boundaryt?

A „schema-less” megnevezés nem jelent szabály nélküli adatot. A schema lehet applicationben,
validation pipeline-ban vagy read-time értelmezésben; ettől a compatibility és quality
felelősség nem tűnik el.

## Polyglot és multi-model

Egy rendszer több modellt használhat: relational system of record, search projection és
analytics warehouse. Ez javíthatja a workload fitet, de növeli a synchronization, lineage,
security és recovery összetettségét. Minden új store-hoz legyen explicit authoritative source,
replication direction és failure policy.

## Források

- [IBM Research — Codd 1970](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks)
- [PostgreSQL 18 — SQL Concepts](https://www.postgresql.org/docs/18/tutorial-concepts.html)
