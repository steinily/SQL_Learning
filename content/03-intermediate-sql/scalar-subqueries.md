---
schema_version: 1
id: DBKB-ISQL-0010
title: Scalar Subqueries
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
related: [DBKB-ISQL-0012, DBKB-SQL-0013]
aliases: [single-row subquery]
search_keywords: [scalar subquery, cardinality, single value]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000033]
acceptance_criteria:
  - Leírja a one-column at-most-one-row contractot.
  - Bemutatja a zero és multiple-row eseteket.
  - Futtatható scalar aggregate példát ad.
---
# Scalar Subqueries

Scalar subquery egy expression helyén pontosan egy columnt szolgáltat. Zero row esetén az eredmény
`NULL`; egynél több row rendszerint cardinality error. Ezért az „első sor” implicit feltételezése
hibás.

```sql
SELECT product_id, unit_price,
       (SELECT AVG(unit_price) FROM product) AS catalog_average
FROM product;
```

Aggregate `GROUP BY` nélkül természetesen egy output sort ad, így jó scalar boundary. `LIMIT 1`
csak akkor korrekt, ha a business rule valóban egy ordered választást kér és teljes deterministic
`ORDER BY` van. Ellenkező esetben adatminőségi hibát rejt el.

Correlated scalar subquery külső soronként más értéket adhat. Olvashatóság vagy performance miatt
átírható join/aggregation formára, de csak azonos duplicate és null semantics bizonyítása után.

A `SQL-ISQL-0010` minden product mellé ugyanazt az exact catalog average-et adja SQLite-on.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
