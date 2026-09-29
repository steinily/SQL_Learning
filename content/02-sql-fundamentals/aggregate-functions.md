---
schema_version: 1
id: DBKB-SQL-0013
title: Aggregate Functions
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
scope: cross-vendor
prerequisites: [DBKB-SQL-0003, DBKB-FND-0017]
related: [DBKB-SQL-0014, DBKB-SQL-0015]
aliases: [aggregation, summary function]
search_keywords: [count, sum, avg, min, max, aggregate]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000027, SRC-000028]
acceptance_criteria:
  - Bemutatja az alap aggregate-eket és input grain változását.
  - Tisztázza a NULL és empty input viselkedést.
  - Futtatható aggregate példát ad.
---
# Aggregate Functions

Aggregate function több input sorból egy group-level értéket számít. Alapformák a `COUNT`, `SUM`,
`AVG`, `MIN` és `MAX`. `GROUP BY` nélkül a teljes filtered input egy group; group key-kkel minden
distinct key combination külön group.

```sql
SELECT COUNT(*) AS row_count,
       SUM(amount) AS total_amount
FROM payment;
```

`COUNT(*)` sorokat számol, míg `COUNT(expression)` a nem-`NULL` expression eredményeket. PostgreSQL
18 dokumentációja szerint a `count` kivételével az általános aggregate-ek empty inputon `NULL`-t
adnak; például a `sum` nem automatikusan zero. Más engine-t és speciális aggregate-et a saját
dokumentációja szerint kell ellenőrizni.

## Grain és type

Aggregation megváltoztatja a result grain-t. Nem-groupolt column nem kerülhet tetszőlegesen a select
listbe; strict SQL ezt elutasítja, egyes konfigurációk engine-specifikus behavior-t engedhetnek.
Numeric aggregate result type-ja eltérhet az input type-tól a range és precision miatt.

Ordered aggregate-eknél az input order jelentést módosíthat; syntaxuk és támogatásuk vendorfüggő.
Performance-ról csak plan, row count és data distribution alapján dönts.

A `SQL-SQL-0013` SQLite fixture `COUNT(*)`, `COUNT(nullable)` és `SUM` exact eredményét ellenőrzi.

## Források

- [PostgreSQL 18 — Aggregate Functions](https://www.postgresql.org/docs/18/functions-aggregate.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
