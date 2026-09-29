---
schema_version: 1
id: DBKB-SQL-0005
title: Column Expressions and Aliases
type: concept
primary_domain: sql-fundamentals
secondary_domains: [foundations]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0003]
related: [DBKB-SQL-0010, DBKB-SQL-0011]
aliases: [select-list expression, column alias]
search_keywords: [expression, alias, as, computed column, qualification]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000024, SRC-000028]
acceptance_criteria:
  - Bemutatja a scalar expression és result alias szerepét.
  - Tisztázza az alias scope és type következményeit.
  - Futtatható számított-column példát ad.
---
# Column Expressions and Aliases

A select-list elem nem csak stored column lehet: literal, arithmetic, function call vagy több elem
összetett expressionje is előállíthat result columnt. Az output type-ot az operand type-ok és a
dialect conversion szabályai határozzák meg.

```sql
SELECT product_name, quantity * unit_price AS line_total
FROM order_line;
```

Az alias az eredmény contract olvasható neve. Használj stabil, jelentést hordozó alias-t API vagy
export felé, és qualifyold az input columnokat több source esetén. Az alias nem írja át a stored
schema-t, és availabilityje más clause-okban dialectfüggő. Portabilityhez ne építs arra, hogy a
`WHERE` ugyanabban a query blockban látja a select-list alias-t; ismételd meg az expressiont vagy
vezess be külön query boundaryt.

## Correctness kérdések

Arithmetic esetén ellenőrizd a numeric precisiont, scale-t, overflow-t és `NULL` propagationt.
Text concatenation operatora és `NULL` kezelése eltérhet. Ugyanazon név használata input és output
alias-ként review- és binding-ambiguityt okozhat.

A `SQL-SQL-0005` SQLite példa exact numeric fixture-rel ellenőrzi a számított total és alias eredményét.
Más engine-en ugyanazt a semantic expectationt a native type-okkal újra kell futtatni.

## Források

- [PostgreSQL 18 Tutorial — Querying a Table](https://www.postgresql.org/docs/18/tutorial-select.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
