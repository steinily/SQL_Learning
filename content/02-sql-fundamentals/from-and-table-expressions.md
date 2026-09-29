---
schema_version: 1
id: DBKB-SQL-0004
title: FROM and Table Expressions
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
scope: cross-vendor
prerequisites: [DBKB-SQL-0003]
related: [DBKB-SQL-0016, DBKB-SQL-0017, DBKB-SQL-0019]
aliases: [table source, table expression]
search_keywords: [from, relation, derived table, alias, join]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000022, SRC-000029]
acceptance_criteria:
  - Meghatározza a FROM szerepét és a table source fogalmát.
  - Bemutatja az alias és qualification használatát.
  - Elkülöníti a logical source-ot a physical access pathtól.
---
# FROM and Table Expressions

A `FROM` clause adja a query table source-ait és azok logical kombinációját. A source lehet base
table, view, derived table, common table expression vagy vendor-specifikus table-valued construct.
A source megnevezése nem mondja meg, hogy az engine table scant, index seeket vagy más physical
operatort választ.

```sql
SELECT p.product_name
FROM product AS p;
```

Az alias rövid, lokális nevet ad. Több source esetén minden columnot érdemes alias-szal qualifyolni:
ez megszünteti az ambiguityt és review során láthatóvá teszi a data lineage-et. Alias után egyes
dialectekben az eredeti table name már nem hivatkozható ugyanabban a query blockban.

Több, join nélkül vesszővel felsorolt source Cartesian productot képezhet. Modern kódban az explicit
`JOIN ... ON` jobban láthatóvá teszi a relationshipet és csökkenti az elhagyott predicate kockázatát.

## Derived table határ

A subquery akkor használható table source-ként, ha table-shaped eredményt ad; rendszerint alias kell.
A benne lévő `ORDER BY` önmagában nem garantálja a külső query sorrendjét. A végső consumer számára
szükséges ordert a legkülső query blockban kell kérni.

A `SQL-SQL-0004` példa aliasolt source projectiont futtat SQLite-on. T-SQL `APPLY`, `PIVOT` és további
table-source formák nem tartoznak e fundamentals topic scope-jába.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [Microsoft — FROM clause plus JOIN, APPLY, PIVOT](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver17)
