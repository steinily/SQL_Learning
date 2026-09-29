---
schema_version: 1
id: DBKB-FND-0010
title: Referential Integrity
type: concept
primary_domain: foundations
secondary_domains: [data-modeling, sql]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0008, DBKB-FND-0009]
related: [DBKB-FND-0011, DBKB-FND-0024, DBKB-FND-0025]
aliases: [foreign key integrity, RI]
search_keywords: [foreign key, parent, child, cascade, restrict, orphan]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0002]
source_ids: [SRC-000009]
acceptance_criteria:
  - Meghatározza a referencing és referenced oldal szerepét.
  - Bemutatja a referential action trade-offokat.
  - Expected-error példával bizonyítja az orphan row elutasítását.
---
# Referential Integrity

A **referential integrity** azt garantálja, hogy a foreign key non-null értéke létező,
engedélyezett referenced keyhez tartozik. A referencing row nem mutathat nem létező parentre.

```sql
CREATE TABLE customer (
    customer_id INTEGER PRIMARY KEY
);

CREATE TABLE sales_order (
    sales_order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
```

PostgreSQL 18 official documentation szerint a foreign key referenced primary keyre, unique
constraintre vagy meghatározott unique indexre mutathat; a pontos lehetőségek vendorfüggők.

## Insert és update

Child insert vagy foreign-key update csak akkor fogadható el, ha a referenced key létezik,
kivéve a megengedett `NULL` esetet. Composite foreign keynél a matching és null handling
szabály (`MATCH`) különösen fontos.

A `SQL-FND-0005` tényleges SQLite expected-error teszt orphan order insertet futtat, és az
`IntegrityError` classt ellenőrzi. Az evidence a deklarált környezetre vonatkozik.

## Delete/update action

- `NO ACTION`/`RESTRICT`: megakadályozza a referenced row változtatását, ha child hivatkozik rá;
  a check timingban lehet különbség.
- `CASCADE`: továbbviszi a delete-et vagy key update-et a childokra.
- `SET NULL`: megszünteti a kapcsolatot; nullable referencing column kell.
- `SET DEFAULT`: default értékre állít, amelynek továbbra is érvényes hivatkozásnak kell lennie.

A `CASCADE` kényelmes, de nagy vagy érzékeny graphban jelentős hatású lehet. Destructive
operation előtt impact query, transaction boundary, authorization és backup/recovery terv kell.

## Performance és lifecycle

A referenced key enforcementjéhez index áll rendelkezésre; a referencing column indexe nem
minden engine-ben automatikus. Parent delete/update child lookupot igényelhet, ezért az access
pattern alapján külön index indokolt lehet. Ez performance döntés, nem a logical foreign key
helyettesítője.

Soft delete esetén a row fizikailag megmarad, így a foreign key önmagában nem tiltja, hogy
aktív child inaktív parentre mutasson. Az „aktívra hivatkozhat” szabályhoz további modeling vagy
transaction protocol kell.

## Forrás

- [PostgreSQL 18 — Constraints / Foreign Keys](https://www.postgresql.org/docs/18/ddl-constraints.html)
