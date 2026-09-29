---
schema_version: 1
id: DBKB-SQL-0009
title: Row Limiting
type: concept
primary_domain: sql-fundamentals
secondary_domains: [performance]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0008]
related: [DBKB-SQL-0003, DBKB-SQL-0013]
aliases: [limit, top, offset fetch, pagination]
search_keywords: [limit, offset, top, fetch, page, keyset]
risk: safe
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000026, SRC-000028]
acceptance_criteria:
  - Elkülöníti a LIMIT és T-SQL row-limiting formákat.
  - Deterministic orderinget követel paginationhöz.
  - Futtatható SQLite LIMIT példát ad.
---
# Row Limiting

Row limiting csak egy result subsetet kér. PostgreSQL és SQLite `LIMIT`/`OFFSET` formát támogat;
T-SQL-ben `TOP`, illetve rendezett paginationhöz `OFFSET ... FETCH` használható. Ezek syntaxa és
bindingja nem portable, ezért a query dialectjét explicit jelölni kell.

```sql
SELECT product_id, product_name
FROM product
ORDER BY product_id
LIMIT 10 OFFSET 20;
```

`ORDER BY` nélkül a kiválasztott subset nem kiszámítható contract. Még ordering mellett is unique
tie-breaker kell, hogy azonos sort key esetén stabil legyen a lap. Concurrent insert/update/delete
mellett offset pagination sorokat ismételhet vagy kihagyhat; erős navigation contracthoz keyset
pagination vagy megfelelő isolation mérlegelendő.

## Performance

Nagy `OFFSET` esetén az engine-nek tipikusan a kihagyott sorokat is elő kell állítania vagy be kell
járnia; a PostgreSQL official dokumentáció ezt külön jelzi. A tényleges költséget data distribution,
index és plan alapján kell mérni. A row limit önmagában nem garantál kis worköt.

A `SQL-SQL-0009` SQLite-on unique `product_id` sorrend mellett ellenőrzi a második két soros lapot.
Ez execution evidence kizárólag a megjelölt SQLite syntaxra érvényes; a PostgreSQL és SQL Server
formák source-verifiedek.

## Források

- [PostgreSQL 18 — LIMIT and OFFSET](https://www.postgresql.org/docs/18/queries-limit.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
