---
schema_version: 1
id: DBKB-ISQL-0011
title: Multi-Row Subqueries
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
prerequisites: [DBKB-ISQL-0009, DBKB-FND-0017]
related: [DBKB-ISQL-0013, DBKB-ISQL-0014]
aliases: [in subquery, any subquery, all subquery]
search_keywords: [in, any, some, all, multi-row subquery]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000033]
acceptance_criteria:
  - Bemutatja az IN ANY SOME ALL formákat.
  - Tárgyalja az empty és NULL input következményeit.
  - Futtatható IN-subquery példát ad.
---
# Multi-Row Subqueries

Multi-row subquery több értéket ad comparison contextnek. `IN` azt kérdezi, van-e equal érték;
`ANY`/`SOME` azt, igaz-e a comparison legalább egy sorra; `ALL` azt, igaz-e minden sorra.

```sql
SELECT product_id
FROM product
WHERE category_id IN (
  SELECT category_id FROM promoted_category
);
```

Az empty subquery és a nullable row-k truth table-je operatoronként fontos. `IN` esetén matching row
`TRUE`; match hiányában egy jobb oldali `NULL` az eredményt `UNKNOWN`-ná teheti. `ALL` empty setre és
`ANY` empty setre adott logikai eredményét konkrét engine documentationnel és teszttel kezeld.

A subquery column type-jának compatible-nek kell lennie a bal expressionnel. Duplicate jobb oldali
érték existence szempontból nem változtatja a logikai választ, de physical worköt befolyásolhat.

A `SQL-ISQL-0011` promoted category listából választ termékeket SQLite-on; null counterexample-t a
`NOT EXISTS and NOT IN` topic külön futtat.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
