---
schema_version: 1
id: DBKB-SQL-0008
title: Ordering with ORDER BY
type: concept
primary_domain: sql-fundamentals
secondary_domains: [foundations]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0003]
related: [DBKB-SQL-0009, DBKB-FND-0020]
aliases: [sorting rows]
search_keywords: [order by, asc, desc, nulls first, nulls last, deterministic]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000025, SRC-000028]
acceptance_criteria:
  - Kimondja, hogy csak az explicit ORDER BY garantál sorrendet.
  - Bemutatja a tie-breaker és NULL ordering szerepét.
  - Futtatható multi-key sort példát ad.
---
# Ordering with ORDER BY

Relációs eredménynek nincs implicit presentation orderje. Garantált sorrendet a query legkülső
szintjén megadott `ORDER BY` definiál. Index order, insertion order vagy egy execution plan korábbi
viselkedése nem result contract.

```sql
SELECT customer_id, created_at
FROM customer
ORDER BY created_at DESC, customer_id ASC;
```

Több sort key lexicographic sorrendet alkot: a következő key csak az előzőn azonos sorok között dönt.
Pagination vagy reproducible export esetén adj unique tie-breakert; különben azonos kulcsú sorok
relatív sorrendje nincs meghatározva.

## Dialect és type kontextus

Az `ASC` és `DESC` irány széles körben támogatott. A `NULL` alapértelmezett helye eltérhet; ahol
támogatott, `NULLS FIRST/LAST`, másutt explicit `CASE` fejezheti ki a contractot. Text ordert a
collation, numeric ordert a type, temporal ordert a timezone-normalization is befolyásolhatja.

Ordinal positionnel (`ORDER BY 2`) rövid a query, de select-list változásra törékeny; tartós kódban
az expression vagy stabil alias olvashatóbb. A sort költségére csak plan és mérés alapján következtess.

A `SQL-SQL-0008` két kulccsal rendez, és exact row sequence-et ellenőriz SQLite-on. A PostgreSQL
`NULL` defaultjára vagy T-SQL viselkedésére ez az evidence nem terjed ki.

## Források

- [PostgreSQL 18 — Sorting Rows](https://www.postgresql.org/docs/18/queries-order.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
