---
schema_version: 1
id: DBKB-ISQL-0021
title: Multiple CTEs
type: concept
primary_domain: intermediate-sql
secondary_domains: [analytics]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0020]
related: [DBKB-ISQL-0002, DBKB-ISQL-0023]
aliases: [chained CTE]
search_keywords: [with, multiple cte, dependency, pipeline]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0003]
source_ids: [SRC-000032]
acceptance_criteria:
  - Bemutatja a CTE dependency chain-t.
  - Minden lépéshez grain contractot követel.
  - Futtatható kétlépcsős CTE példát ad.
---
# Multiple CTEs

Egy `WITH` clause több névvel ellátott queryt definiálhat. Egy későbbi CTE hivatkozhat korábbira;
így data-flow olvasható lépésekre bontható.

```sql
WITH order_totals AS (...),
customer_totals AS (
  SELECT customer_id, SUM(order_total) AS total
  FROM order_totals
  GROUP BY customer_id
)
SELECT * FROM customer_totals;
```

Minden boundaryn dokumentáld a key-t, grain-t, nullable columnokat és row-count expectationt. A túl
hosszú „CTE pipeline” elrejtheti a cardinality változásokat; ilyenkor bontsd view-ra vagy staged
transformationre, ha reuse és governance indokolja.

A definition order és forward-reference support dialectfüggő lehet. A multiple CTE syntax nem ígér
execution ordert vagy külön materializationt. Side effect és evaluation count nem lehet üzleti logic.

A `SQL-ISQL-0021` előbb order, majd customer grainre aggregál, és exact totalokat ellenőriz SQLite-on.

## Források

- [PostgreSQL 18 — WITH Queries](https://www.postgresql.org/docs/18/queries-with.html)
