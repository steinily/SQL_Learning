---
schema_version: 1
id: DBKB-SQL-0014
title: GROUP BY
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
prerequisites: [DBKB-SQL-0013]
related: [DBKB-SQL-0015, DBKB-SQL-0012]
aliases: [grouping]
search_keywords: [group by, group key, grain, aggregate]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000027, SRC-000028]
acceptance_criteria:
  - Meghatározza a group key és output grain kapcsolatát.
  - Megkülönbözteti a row és group filtert.
  - Futtatható grouping példát ad.
---
# GROUP BY

A `GROUP BY` az input sorokat azonos key combination alapján groupokra osztja. Az output grain a
group key: normál select-list elemként csak group key vagy aggregate érték jelenjen meg.

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM sales_order
GROUP BY customer_id
ORDER BY customer_id;
```

Groupolás előtt a `WHERE` sorokat távolít el; groupolás után a `HAVING` groupokat. Ez semantic
különbség, nem pusztán syntax. Ha az intent egyedi sorok listája aggregate nélkül, `DISTINCT` lehet
közvetlenebb; ha measure kell, a grain-t és minden measure aggregation szabályát külön nevezd meg.

## Correctness

Join után groupolva előbb ellenőrizd, hogy a join nem sokszorozta-e a measure row-kat. Egy order header
és több line joinja például helyes line totalhoz, de hibás lehet header-level amount összegzéséhez.
Nullable group key-k egy külön null groupot alkothatnak; ez nem azonos a `NULL = NULL` predicate-tel.

Advanced grouping set, rollup és cube syntax vendor/version-sensitive, és nem része ennek az alap
portable példának. A `SQL-SQL-0014` exact customer-level countot futtat SQLite-on.

## Források

- [PostgreSQL 18 — Aggregate Functions](https://www.postgresql.org/docs/18/functions-aggregate.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
