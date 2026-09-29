---
schema_version: 1
id: DBKB-SQL-0006
title: Filtering with WHERE
type: concept
primary_domain: sql-fundamentals
secondary_domains: [foundations]
levels: [beginner]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: portable-sql
prerequisites: [DBKB-SQL-0003, DBKB-FND-0017]
related: [DBKB-SQL-0007, DBKB-SQL-0015, DBKB-SQL-0021]
aliases: [row filter]
search_keywords: [where, predicate, filter, "null", boolean]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000022, SRC-000024]
acceptance_criteria:
  - Elmagyarázza a WHERE true-only row selectionját.
  - Bemutatja a NULL és operator precedence veszélyeit.
  - Futtatható filter példát ad.
---
# Filtering with WHERE

A `WHERE` clause row-level predicate-et alkalmaz. Csak azok a sorok maradnak meg, amelyekre a
predicate eredménye `TRUE`; a `FALSE` és `UNKNOWN` sorok kiesnek. Emiatt a nullable columnra írt
egyszerű comparison nem találja meg a `NULL` értékeket.

```sql
SELECT order_id, status
FROM sales_order
WHERE status = 'OPEN';
```

`NULL` vizsgálatához `IS NULL` vagy `IS NOT NULL` kell, nem `= NULL`. Több condition esetén zárójelekkel
tedd explicit-té az `AND` és `OR` kívánt groupingját. A precedence ismerete nem helyettesíti az
olvashatóságot.

## Sargability és correctness

A filter semantic helyessége az első. Performance szempontból columnra alkalmazott function vagy
implicit conversion megakadályozhat előnyös access pathot, de ezt plan evidence nélkül ne állítsd
biztosan. Date/time range-nél a fél-nyílt intervallum gyakran egyértelmű: `created_at >= start` és
`created_at < end`.

Outer join esetén a nullable oldalra a `WHERE`-ben tett condition eldobhatja az unmatched sorokat;
ha a match feltétele, gyakran az `ON` clause-ba tartozik. `UPDATE` és `DELETE` esetén ugyanaz a
`WHERE` már destructive boundary, ezért preview és transaction szükséges.

A `SQL-SQL-0006` example equality és range condition együttes eredményét ellenőrzi SQLite-on.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [PostgreSQL 18 Tutorial — Querying a Table](https://www.postgresql.org/docs/18/tutorial-select.html)
