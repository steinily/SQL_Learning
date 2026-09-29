---
schema_version: 1
id: DBKB-ISQL-0023
title: Derived Tables
type: concept
primary_domain: intermediate-sql
secondary_domains: [sql-fundamentals]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: portable-sql
prerequisites: [DBKB-ISQL-0009, DBKB-SQL-0004]
related: [DBKB-ISQL-0020, DBKB-ISQL-0024]
aliases: [from subquery, inline view]
search_keywords: [derived table, subquery in from, alias, query boundary]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0003]
source_ids: [SRC-000036]
acceptance_criteria:
  - FROM-scoped table expressionként definiálja a derived table-t.
  - Megköveteli az alias és output grain tisztázását.
  - Futtatható pre-aggregation példát ad.
---
# Derived Tables

Derived table a `FROM` clause-ban álló parenthesized subquery. Table-shaped resultot ad az enclosing
querynek, és stabil boundaryt képezhet aggregation, filtering vagy column naming számára.

```sql
SELECT d.customer_id, d.total
FROM (
  SELECT customer_id, SUM(amount) AS total
  FROM sales_order
  GROUP BY customer_id
) AS d
WHERE d.total >= 100;
```

Adj alias-t a derived table-nek és egyértelmű neveket az output expressionöknek. A belső query grainje
az outer query input grainje; ezt review során külön rögzítsd.

A derived table statement-scoped és nem feltétlen materialized. Correlated table expressionhöz egyes
engine-ek `LATERAL` vagy `APPLY` syntaxot igényelnek, ami M04 téma. Belső ordering nem garantálja a
külső result sorrendjét.

A `SQL-ISQL-0023` pre-aggregált customer totalból threshold alapján választ SQLite-on.

## Források

- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
