---
schema_version: 1
id: DBKB-FND-0009
title: Relationships
type: concept
primary_domain: foundations
secondary_domains: [data-modeling]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: [portable-sql]
scope: general
prerequisites: [DBKB-FND-0006, DBKB-FND-0008]
related: [DBKB-FND-0010, DBKB-FND-0021, DBKB-FND-0023]
aliases: [one-to-one, one-to-many, many-to-many, association]
search_keywords: [cardinality, optionality, foreign key, junction table]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0002]
source_ids: [SRC-000002, SRC-000009]
acceptance_criteria:
  - Bemutatja a cardinality és optionality szerepét.
  - Megmutatja a relationship relational reprezentációját.
  - Elkülöníti a conceptual kapcsolatot a physical enforcementtől.
---
# Relationships

A **relationship** azt fejezi ki, hogy két vagy több entity előfordulásai hogyan tartoznak
össze. A conceptual modelben nevük, cardinalityjük és optionalityjük van; a relational
implementationben key value-k és constraint-ek reprezentálják őket.

## Cardinality és optionality

- **One-to-one:** egy A legfeljebb egy B-hez, és fordítva. Foreign key plusz `UNIQUE` gyakori
  enforcement.
- **One-to-many:** egy parenthez több child tartozhat; a foreign key tipikusan a childban van.
- **Many-to-many:** mindkét oldalon több kapcsolat lehet; junction/association table bontja két
  one-to-many kapcsolatra.

Az **optionality** külön kérdés: kötelező-e a kapcsolat? Nullable foreign key optional
relationshipet engedhet; `NOT NULL` kötelezővé teszi a referencing value-t, de csak a foreign
key bizonyítja, hogy a referenced row létezik.

## Many-to-many példa

```sql
CREATE TABLE product_supplier (
    product_id INTEGER NOT NULL REFERENCES product(product_id),
    supplier_id INTEGER NOT NULL REFERENCES supplier(supplier_id),
    supplier_sku VARCHAR(40),
    PRIMARY KEY (product_id, supplier_id)
);
```

A junction table saját attribute-okat is hordozhat. Ha a kapcsolatnak price, validity vagy
status tulajdonsága van, nem puszta technikai híd, hanem önálló association entity.

## Direction és ownership

A foreign key direction nem feltétlenül az adatfolyam directionje. A child hivatkozik a
parentre, de mindkét oldalról lehet queryzni. `ON DELETE` policyvel explicit döntjük el, hogy a
parent eltávolítása tiltott, propagált vagy a hivatkozás nullázott legyen. A default vak
elfogadása helyett az entity lifecycle alapján válassz.

## Idő és kapcsolat

Egy kapcsolat időben változhat. Ha történet kell, a jelenlegi foreign key felülírása helyett
validity intervalt vagy history relationt használunk. Ilyenkor az „egy aktív kapcsolat” szabály
gyakran összetettebb constraintet és transaction-safe update protocolt kíván.

## Gyakori modeling hibák

- comma-separated ID-k egy text columnban;
- több nullable foreign key közül „pontosan egy” szabály nélkül;
- polymorphic `object_type + object_id` database-level referential integrity nélkül;
- many-to-many kapcsolat közvetlenül, association key nélkül;
- conceptual cardinality dokumentálása enforcement nélkül.

## Források

- [IBM Research — Codd relational model](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks)
- [PostgreSQL 18 — Foreign Keys](https://www.postgresql.org/docs/18/ddl-constraints.html)
