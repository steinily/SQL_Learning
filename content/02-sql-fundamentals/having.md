---
schema_version: 1
id: DBKB-SQL-0015
title: HAVING
type: concept
primary_domain: sql-fundamentals
secondary_domains: [analytics]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: portable-sql
prerequisites: [DBKB-SQL-0014]
related: [DBKB-SQL-0006, DBKB-SQL-0013]
aliases: [group filter]
search_keywords: [having, aggregate filter, group predicate]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000027, SRC-000028]
acceptance_criteria:
  - Elkülöníti a HAVING és WHERE felelősségét.
  - Aggregate predicate-et mutat be.
  - Futtatható group-filter példát ad.
---
# HAVING

A `HAVING` group-level predicate. Akkor használd, amikor a feltétel aggregate eredményre vagy a
group egészére vonatkozik. A `WHERE` ezzel szemben az aggregation előtti input sorokat szűri.

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM sales_order
WHERE status = 'OPEN'
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

Itt először csak az `OPEN` sorok maradnak, majd customer groupok képződnek, végül csak legalább két
ilyen orderrel rendelkező customer marad. Ha a `status` conditiont `HAVING`-be mozgatnánk, más vagy
érvénytelen semanticset kaphatnánk.

## Review

Ellenőrizd az input grain-t, a group key-t és az aggregate denominatorát. `HAVING` nem általános
helyettesítője a `WHERE`-nek. A row-level condition korai szűrése gyakran egyszerűbb intentet ad;
optimizer rewrite lehetőségéről és performance-ról plan nélkül ne tegyél engine-specifikus ígéretet.

Aggregate alias használata `HAVING`-ben dialectfüggő lehet. Portable kódban ismételd meg az aggregate
expressiont vagy használj külön query boundaryt. `NULL` aggregate eredményre a three-valued logic
ugyanúgy érvényes.

A `SQL-SQL-0015` SQLite-on két groupból csak a thresholdot elérőt adja vissza.

## Források

- [PostgreSQL 18 — Aggregate Functions](https://www.postgresql.org/docs/18/functions-aggregate.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
