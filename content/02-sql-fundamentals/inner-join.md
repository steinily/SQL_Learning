---
schema_version: 1
id: DBKB-SQL-0017
title: INNER JOIN
type: concept
primary_domain: sql-fundamentals
secondary_domains: [data-modeling]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: portable-sql
prerequisites: [DBKB-SQL-0016]
related: [DBKB-SQL-0018, DBKB-SQL-0019]
aliases: [equi-join]
search_keywords: [inner join, match, "on", equijoin]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000029]
acceptance_criteria:
  - Elmagyarázza az INNER JOIN matched-row semanticsét.
  - Bemutatja a duplicate és NULL key következményeit.
  - Futtatható inner join példát ad.
---
# INNER JOIN

Az `INNER JOIN` csak olyan kombinációkat tart meg, amelyekre az `ON` predicate `TRUE`. Az egyik
oldalon unmatched sor nem jelenik meg. Az `INNER` keyword rendszerint elhagyható, de explicit
használata oktatási vagy style okból hasznos lehet.

```sql
SELECT o.order_id, c.customer_name
FROM sales_order AS o
INNER JOIN customer AS c
  ON c.customer_id = o.customer_id;
```

Ha egy key mindkét oldalon többször fordul elő, minden matching kombináció létrejön. Ez nem engine
hiba, hanem join cardinality. A helyes megoldás a model és intent tisztázása, nem automatikus
`DISTINCT`.

Equality join nullable key-jén a `NULL = NULL` nem `TRUE`, ezért ezek a sorok nem match-elnek.
Null-safe equality operatorok vendorfüggők; használatukat explicit dialect scope-pal kell dokumentálni.

## `ON` és `WHERE`

Inner join esetén bizonyos filterek áthelyezése az `ON` és `WHERE` között azonos resultot adhat, de a
relationship és a row filter külön írása olvashatóbb intentet nyújt. Outer joinra ugyanez az áthelyezés
nem általánosan ekvivalens.

A `SQL-SQL-0017` két customer és három order fixture-ből a három matched sort exact sorrendben
ellenőrzi SQLite-on.

## Források

- [Microsoft — FROM clause plus JOIN](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver17)
