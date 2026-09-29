---
schema_version: 1
id: DBKB-ISQL-0007
title: Semi Joins
type: concept
primary_domain: intermediate-sql
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0017, DBKB-ISQL-0005]
related: [DBKB-ISQL-0008, DBKB-ISQL-0013]
aliases: [existence join]
search_keywords: [semi join, exists, in, existence, cardinality]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0001]
source_ids: [SRC-000033]
acceptance_criteria:
  - Meghatározza a left-row-preserving existence semanticset.
  - Elkülöníti az EXISTS mintát az inner join plusz DISTINCT-től.
  - Futtatható semi-join példát ad.
---
# Semi Joins

Logical semi join azokat a bal oldali sorokat adja vissza, amelyekhez legalább egy jobb oldali match
létezik. A jobb oldal columnjai nem részei az outputnak, és több match sem sokszorozza a bal sort.
Portable SQL-ben tipikus forma a correlated `EXISTS`.

```sql
SELECT c.customer_id
FROM customer AS c
WHERE EXISTS (
  SELECT 1
  FROM sales_order AS o
  WHERE o.customer_id = c.customer_id
);
```

Az `EXISTS` select listjének értéke általában nem számít; a kérdés csak az, visszaad-e sort. Ne tegyél
side effectet a subquerybe, és ne feltételezd az evaluation countot. `IN` is kifejezhet existence-et,
de `NULL`, composite key és type coercion miatt külön review kell.

Inner join plusz `DISTINCT` gyakran drágább vagy félrevezető, és elveszíti annak jelzését, hogy csak
existence volt a kérdés. A physical semi-join operator használata optimizer döntés.

A `SQL-ISQL-0007` olyan customereket ad vissza, akiknek legalább egy orderük van, minden customert
legfeljebb egyszer.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
