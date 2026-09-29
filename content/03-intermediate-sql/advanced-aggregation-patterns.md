---
schema_version: 1
id: DBKB-ISQL-0002
title: Advanced Aggregation Patterns
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
prerequisites: [DBKB-SQL-0013, DBKB-SQL-0014]
related: [DBKB-ISQL-0003, DBKB-ISQL-0004]
aliases: [multi-stage aggregation]
search_keywords: [aggregate, grain, pre-aggregation, ratio, weighted average]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0001]
source_ids: [SRC-000027, SRC-000036]
acceptance_criteria:
  - Bemutatja a multi-stage aggregation és grain kontroll szerepét.
  - Megkülönbözteti a ratio of sums és average of ratios kérdést.
  - Futtatható pre-aggregation példát ad.
---
# Advanced Aggregation Patterns

Advanced aggregationnél a fő kérdés nem a function neve, hanem hogy **milyen grain-en** számolunk.
Join előtt pre-aggregate-elj, ha a részletes oldal megsokszorozná a másik oldal measure-jét. Többlépcsős
számításnál egy derived table vagy CTE rögzíti az intermediate grain-t.

```sql
WITH order_totals AS (
  SELECT order_id, SUM(quantity * unit_price) AS order_total
  FROM order_line
  GROUP BY order_id
)
SELECT AVG(order_total) FROM order_totals;
```

Az `AVG(quantity * price)` line-weighted átlagot, az orderenkénti totalok `AVG`-je order-weighted
átlagot ad. Hasonlóan, `SUM(numerator) / SUM(denominator)` általában nem azonos a soronkénti ratio-k
átlagával. A business definíció dönt.

Empty group, nullable measure, zero denominator, integer division és numeric precision mind explicit
policyt igényel. `COUNT(*)` és `COUNT(expression)` különbségét minden completeness metricnél jelöld.
Physical aggregate algorithmot csak planből állíts.

A `SQL-ISQL-0002` két order line-jait előbb order grainre összegzi, majd exact average-et ellenőriz
SQLite-on.

## Források

- [PostgreSQL 18 — Aggregate Functions](https://www.postgresql.org/docs/18/functions-aggregate.html)
- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
