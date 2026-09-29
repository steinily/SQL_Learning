---
schema_version: 1
id: DBKB-SQL-0003
title: SELECT Fundamentals
type: concept
primary_domain: sql-fundamentals
secondary_domains: [foundations]
levels: [beginner]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: portable-sql
prerequisites: [DBKB-SQL-0002]
related: [DBKB-SQL-0004, DBKB-SQL-0005, DBKB-SQL-0006, DBKB-SQL-0008]
aliases: [projection query]
search_keywords: [select, projection, result set, column]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000022, SRC-000024]
acceptance_criteria:
  - Bemutatja a SELECT list és result set kapcsolatát.
  - Elmagyarázza a csillag projection kockázatait.
  - Futtatható, elvárt eredményű példát ad.
---
# SELECT Fundamentals

A `SELECT` query result setet állít elő. A select list határozza meg a result columnokat és azok
sorrendjét; minden elem column reference, literal vagy expression lehet. A source nélküli constant
query támogatása dialectfüggő, ezért portable adatlekérdezéshez explicit table source a biztos alap.

```sql
SELECT product_id, product_name, unit_price
FROM product;
```

A `SELECT *` gyors exploratory eszköz, de tartós interface-ben törékeny: schema változáskor módosulhat
a shape, felesleges adatot olvashat, és azonos nevű join columnokat tehet kétértelművé. Nevezd meg a
szükséges columnokat, különösen application boundaryn és view definícióban.

`SELECT` önmagában nem ígér row ordert. A tárolási sorrend, egy index jelenléte vagy egy korábbi run
eredménye nem contract. Ha a sorrend jelentéssel bír, adj teljes `ORDER BY`-t.

## Ellenőrzési minta

Vizsgáld a result schema-t, a cardinalityt és az értékeket külön. Empty result nem feltétlen hiba;
lehet helyes következménye a filternek. Duplicate row is lehet helyes, mert a SQL result alapértelmezés
szerint nem set-deduplicationt alkalmaz; erre szolgál az explicit `DISTINCT`.

A kapcsolódó `SQL-SQL-0003` példa ephemeral SQLite adatbázison igazolja a projection resultját.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [PostgreSQL 18 Tutorial — Querying a Table](https://www.postgresql.org/docs/18/tutorial-select.html)
