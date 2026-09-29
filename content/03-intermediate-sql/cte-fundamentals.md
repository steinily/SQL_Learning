---
schema_version: 1
id: DBKB-ISQL-0020
title: CTE Fundamentals
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
scope: cross-vendor
prerequisites: [DBKB-ISQL-0009]
related: [DBKB-ISQL-0021, DBKB-ISQL-0022, DBKB-ISQL-0023]
aliases: [common table expression, with query]
search_keywords: [with, cte, named query, query decomposition]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0003]
source_ids: [SRC-000032]
acceptance_criteria:
  - Statement-scoped named queryként definiálja a CTE-t.
  - Nem feltételez univerzális materializationt.
  - Futtatható CTE példát ad.
---
# CTE Fundamentals

A common table expression a `WITH` clause-ban nevet ad egy auxiliary statement eredményének a
következő primary statement scope-jára. Olvasható lépésekre bonthatja a queryt és explicit intermediate
grain-t rögzíthet.

```sql
WITH order_totals AS (
  SELECT order_id, SUM(quantity * unit_price) AS total
  FROM order_line
  GROUP BY order_id
)
SELECT order_id, total FROM order_totals;
```

A CTE nem permanent object és nem reusable más statementből. Nem univerzálisan temporary table,
materialized result vagy optimization fence: inline/materialize behavior engine- és verziófüggő.
Performance következtetéshez execution plan kell.

Ne használj CTE-t csupán nesting növelésére. Minden lépésnek legyen világos neve, grain-je és
column contractja. Multiple reference esetén az evaluation és reuse behavior-t külön ellenőrizd.

A `SQL-ISQL-0020` order total CTE eredményét exact sorokkal validálja SQLite-on.

## Források

- [PostgreSQL 18 — WITH Queries](https://www.postgresql.org/docs/18/queries-with.html)
