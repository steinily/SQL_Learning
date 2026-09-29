---
schema_version: 1
id: DBKB-SQL-0012
title: DISTINCT
type: concept
primary_domain: sql-fundamentals
secondary_domains: [data-quality]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: portable-sql
prerequisites: [DBKB-SQL-0003]
related: [DBKB-SQL-0013, DBKB-SQL-0016, DBKB-FND-0019]
aliases: [duplicate elimination]
search_keywords: [distinct, duplicate, projection, uniqueness]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000024, SRC-000028]
acceptance_criteria:
  - Elmagyarázza a full result-row duplicate eliminationt.
  - Elkülöníti a DISTINCT használatát a join hiba elfedésétől.
  - Futtatható duplicate-elimination példát ad.
---
# DISTINCT

A `SELECT DISTINCT` azonos result row-kból egyet tart meg. Az összehasonlítás a teljes select listre
vonatkozik: ha bármely output column eltér, a sorok különbözők. A művelet nem garantál sorrendet;
presentation orderhez továbbra is explicit `ORDER BY` kell.

```sql
SELECT DISTINCT customer_id
FROM sales_order
ORDER BY customer_id;
```

`DISTINCT` helyes, amikor a kérdés valóban unique értékkombinációt kér. Nem jó alapértelmezett javítás
egy hibás join sokszorozódására: elfedheti a hiányzó join predicate-et, rossz cardinality assumptiont
vagy data-quality problémát. Előbb bizonyítsd a source grain-t és relationshipet.

## `NULL` és performance

Duplicate elimination szempontjából a query engine az azonos output tuple-öket vonja össze; a
`NULL`-okat tartalmazó sorok viselkedését ne keverd a `WHERE` three-valued comparisonjával. A physical
megvalósítás lehet sort, hash vagy más operator; konkrét algoritmust csak plan evidence alapján nevezz.

Ha pusztán existence a kérdés, gyakran `EXISTS` fejezi ki pontosabban az intentet, mint egy join plusz
`DISTINCT`. Aggregate contextben a `COUNT(DISTINCT expression)` más művelet és null-kezelését külön
kell ellenőrizni.

A `SQL-SQL-0012` SQLite példa ismétlődő customer id-kből exact unique resultot állít elő.

## Források

- [PostgreSQL 18 Tutorial — Querying a Table](https://www.postgresql.org/docs/18/tutorial-select.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
