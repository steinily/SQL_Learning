---
schema_version: 1
id: DBKB-FND-0007
title: Tables Rows and Columns
type: concept
primary_domain: foundations
secondary_domains: [sql, data-modeling]
levels: [beginner]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0006]
related: [DBKB-FND-0008, DBKB-FND-0012, DBKB-FND-0023, DBKB-FND-0035]
aliases: [table, row, column, record, field]
search_keywords: [relation, tuple, attribute, heading, row order]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0002]
source_ids: [SRC-000003, SRC-000009]
acceptance_criteria:
  - Pontosan leírja a table, row és column szerepét.
  - Kiemeli az explicit key, type és order szükségességét.
  - Runnable CREATE/INSERT/SELECT példát ad.
---
# Tables Rows and Columns

A relational SQL database-ben a **table** named szerkezet; **columnjai** nevet és data type-ot
adnak az attribute-oknak, **row-jai** pedig konkrét állításokat hordoznak. A PostgreSQL 18
Concepts dokumentáció ugyanezt a named row collection és named typed column képet használja.

## Table definition

```sql
CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    sku VARCHAR(30) NOT NULL UNIQUE,
    product_name VARCHAR(200) NOT NULL,
    unit_price DECIMAL(12, 2) NOT NULL CHECK (unit_price >= 0)
);
```

A definition nem csak column list: identityt és invariantokat is rögzít. A `DECIMAL(12,2)`
representation önmagában nem tiltja a negatív árat, ezért külön `CHECK` szükséges.

## Row mint állítás

```sql
INSERT INTO product (product_id, sku, product_name, unit_price)
VALUES (1001, 'BRG-6204', 'Bearing 6204', 12.50);
```

Az explicit column lista ellenállóbb a column order változásával szemben. A row identityt nem
a fizikai pozíció, hanem a deklarált key adja. „Az első row” vagy „a következő row” csak
explicit ordering vagy cursor/protocol kontextusban értelmes.

## Nincs implicit row order

```sql
SELECT product_id, product_name
FROM product
ORDER BY product_id;
```

`ORDER BY` nélkül az engine nem garantál row ordert. Egy index scan vagy új execution plan
megváltoztathatja a látszólag stabil sorrendet. Determinisztikus outputhoz olyan ordering key
kell, amely a tie-okat is feloldja.

## Column design

A jó column név jelentést közöl, a type reprezentációt és operation setet választ, a constraint
pedig megengedett state-et szűkít. A nullable állapotot tudatosan kell kezelni; részleteit a
[NULL Fundamentals](null-fundamentals.md) tárgyalja.

Kerüld a több értéket elrejtő comma-separated textet, ha az elemekre külön integrity vagy query
kell. Ugyanakkor nem minden nested structure igényel külön table-t: az aggregate boundary és
access pattern dönt.

A `SQL-FND-0004` example a definitiont, insertet, key-alapú lookupot és expected row-t tényleges
SQLite futtatással ellenőrzi a deklarált portable subsetben.

## Források

- [PostgreSQL 18 — SQL Concepts](https://www.postgresql.org/docs/18/tutorial-concepts.html)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
