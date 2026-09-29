---
schema_version: 1
id: DBKB-FND-0018
title: Sets
type: concept
primary_domain: foundations
secondary_domains: [mathematics, sql]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: [portable-sql]
scope: general
prerequisites: [DBKB-FND-0002]
related: [DBKB-FND-0006, DBKB-FND-0019, DBKB-FND-0020]
aliases: [set, member, subset]
search_keywords: [union, intersection, difference, Cartesian product, duplicate]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0003]
source_ids: [SRC-000002]
acceptance_criteria:
  - Ismerteti a set, membership és alapműveletek fogalmát.
  - Kapcsolja a halmazt a relation fogalmához.
  - Elkülöníti a mathematical setet az SQL bag behaviorétől.
---
# Sets

A **set** különböző elemek rendezetlen gyűjteménye. Egy elem vagy tag (`∈`), vagy nem tag; az
ismételt felsorolás nem hoz létre új példányt, és az order nem része a set identitynek.

## Alapműveletek

- **Union (`A ∪ B`):** ami A-ban vagy B-ben szerepel.
- **Intersection (`A ∩ B`):** ami mindkettőben szerepel.
- **Difference (`A − B`):** ami A-ban igen, B-ben nem.
- **Cartesian product (`A × B`):** minden A–B rendezett pár.
- **Subset (`A ⊆ B`):** A minden eleme B-nek is eleme.

## Relation mint set

A formal relation azonos headinggel rendelkező tuple-ök setje. Nincs duplicate tuple és nincs
implicit tuple order. Codd modellje erre a matematikai alapra építi az n-ary relationöket és
műveleteiket.

## SQL bag eltérés

SQL query result alapértelmezésben duplicate row-kat is tartalmazhat, tehát gyakran **bag** vagy
multiset semanticsot követ. `UNION` duplicate eliminationt végez, `UNION ALL` megtartja az
előfordulásokat. `SELECT DISTINCT` szintén duplicate elimination, amelynek execution costja
lehet.

```sql
SELECT code FROM source_a
UNION
SELECT code FROM source_b;
```

A set operation általában union-compatible inputot igényel: egyező column count és kompatibilis
type-ok. Column name és ordering dialect behaviorét külön ellenőrizd.

## Gyakorlati következmény

Ha duplicate üzletileg hiba, ne csak a final queryben használj `DISTINCT`-et. Határozd meg az
identityt és védd key/unique constrainttel a canonical storage-ban. A `DISTINCT` elrejtheti a
rossz join cardinalityt vagy többszörös ingestiont.

## Forrás

- [IBM Research — Codd relational model](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks)
