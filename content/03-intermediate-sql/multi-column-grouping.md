---
schema_version: 1
id: DBKB-ISQL-0004
title: Multi-Column Grouping
type: concept
primary_domain: intermediate-sql
secondary_domains: [analytics, data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: portable-sql
prerequisites: [DBKB-SQL-0014, DBKB-FND-0019]
related: [DBKB-ISQL-0002, DBKB-SQL-0015]
aliases: [composite grouping key]
search_keywords: [group by, composite grain, dimension, null group]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0001]
source_ids: [SRC-000027, SRC-000036]
acceptance_criteria:
  - Composite keyként magyarázza a több-column groupingot.
  - Bemutatja a grain és functional dependency kérdését.
  - Futtatható két-dimenziós grouping példát ad.
---
# Multi-Column Grouping

Több `GROUP BY` column együtt composite group key-t alkot. Az output grain például nem egyszerűen
„nap” vagy „region”, hanem `(order_day, region_code)`.

```sql
SELECT order_day, region_code, SUM(amount) AS amount
FROM sales_order
GROUP BY order_day, region_code;
```

Minden további key finomíthatja a grain-t és növelheti a groupok számát. A select listben szereplő
nem-aggregate attributumnak group keynek vagy az engine által bizonyítható functional dependency
alapján engedettnek kell lennie; utóbbi supportja és szabálya vendorfüggő, ezért portable kódban
groupold explicit módon.

Nullable key esetén a `NULL` értékű sorok egy groupba kerülnek az adott key combinationön belül.
Ez aggregation grouping rule, nem annak állítása, hogy `NULL = NULL` predicate `TRUE`.

Date/time groupingnál rögzítsd a timezone-t és a period boundaryt. Text dimensionnél a collation
befolyásolhatja, mi számít azonosnak. A `SQL-ISQL-0004` két region és két nap composite groupjait
ellenőrzi SQLite-on.

## Források

- [PostgreSQL 18 — Aggregate Functions](https://www.postgresql.org/docs/18/functions-aggregate.html)
- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
