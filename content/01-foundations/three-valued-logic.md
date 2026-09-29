---
schema_version: 1
id: DBKB-FND-0017
title: Three-Valued Logic
type: concept
primary_domain: foundations
secondary_domains: [sql]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0016]
related: [DBKB-FND-0011, DBKB-FND-0020]
aliases: [3VL, TRUE FALSE UNKNOWN]
search_keywords: [boolean, predicate, AND, OR, NOT, WHERE, "NULL"]
risk: safe
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0003]
source_ids: [SRC-000004, SRC-000005]
acceptance_criteria:
  - Bemutatja a TRUE, FALSE és UNKNOWN truth table lényegét.
  - Megmagyarázza a WHERE és CHECK eltérő acceptance contextjét.
  - Execution-verified predicate példát ad.
---
# Three-Valued Logic

SQL predicate eredménye lehet `TRUE`, `FALSE` vagy `UNKNOWN`. Az `UNKNOWN` tipikusan akkor
keletkezik, amikor ordinary comparison egyik operandusa `NULL`. A PostgreSQL 18 official
logical-operator dokumentációja explicit truth table-t közöl.

## Alapszabályok

| A | `NOT A` |
|---|---|
| TRUE | FALSE |
| FALSE | TRUE |
| UNKNOWN | UNKNOWN |

`FALSE AND UNKNOWN` eredménye `FALSE`, mert a másik operandustól függetlenül nem lehet true.
`TRUE OR UNKNOWN` eredménye `TRUE`. Más kombinációkban az unknown megmaradhat.

## Filtering context

A `WHERE`, `HAVING` és join condition csak `TRUE` esetén tartja meg a row-t. `FALSE` és
`UNKNOWN` egyaránt kiesik:

```sql
WHERE status <> 'CANCELLED'
```

nem választja ki a `status IS NULL` row-kat. Ha az unknown is kell, explicit `OR status IS NULL`
szükséges.

## Constraint context

PostgreSQL `CHECK` constraintje `FALSE` esetén sérül; `TRUE` és `UNKNOWN` elfogadott. Ezért a
nullabilityt külön `NOT NULL` védi. Ugyanaz a predicate tehát filtering és constraint
contextben eltérő acceptance hatást adhat.

## NOT IN csapda

Ha a `NOT IN` list/subquery `NULL`-t tartalmaz, az összehasonlítás UNKNOWN-ná válhat, és várt
row-k eshetnek ki. Gyakran `NOT EXISTS` és explicit correlated predicate a tisztább forma, de
duplikátum, nullability és dialect semantics review szükséges.

A `SQL-FND-0008` `VALUES` fixture-rel futtat `IS NULL`, equality és inequality predicate-eket,
és expected resulttal ellenőrzi a filtering hatást.

## Források

- [PostgreSQL 18 — Logical Operators](https://www.postgresql.org/docs/18/functions-logical.html)
- [PostgreSQL 18 — Comparison Functions](https://www.postgresql.org/docs/18/functions-comparison.html)
