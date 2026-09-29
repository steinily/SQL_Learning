---
schema_version: 1
id: DBKB-SQL-0020
title: INSERT
type: concept
primary_domain: sql-fundamentals
secondary_domains: [data-integrity]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0002, DBKB-FND-0010]
related: [DBKB-SQL-0021, DBKB-SQL-0022]
aliases: [insert row, data creation]
search_keywords: [insert, values, column list, constraint, transaction]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000031, SRC-000030]
acceptance_criteria:
  - Bemutatja az explicit-column INSERT formát.
  - Tárgyalja a constraint, default és transaction szerepét.
  - Futtatható insert-and-readback példát ad.
---
# INSERT

Az `INSERT` új sorokat ad a target table-höz. Tartós kódban explicit column listet használj, hogy a
statement ne függjön rejtetten a physical column ordertől.

```sql
INSERT INTO customer (customer_id, customer_name)
VALUES (101, 'Ada');
```

Az elhagyott column értékét default, generated value vagy `NULL` adhatja, ha a schema engedi. A
constraint-ek a statement során integrityt ellenőriznek; a pontos timing és multi-row failure behavior
engine- és transaction-specifikus. Generated key visszaadása (`RETURNING`, `OUTPUT` vagy API) szintén
dialectfüggő.

## Input és idempotency

Parameterizáld az értékeket, és a client driveren keresztül add át type-helyesen. Ne illessz user textet
SQL stringbe. Retry esetén egy nem idempotens insert duplikálhat; business key, request id vagy
documentált upsert strategy kell, utóbbi syntaxa vendor-specific.

Bulk load, `INSERT ... SELECT`, conflict handling és identity override külön advanced témák. Minden
loadnál ellenőrizd a requested, inserted, rejected és committed row countot.

A `SQL-SQL-0020` ephemeral SQLite adatbázisban beszúr egy sort, majd readbackkel ellenőrzi. Az evidence
nem állít PostgreSQL `RETURNING` vagy T-SQL `OUTPUT` execution supportot.

## Források

- [PostgreSQL 18 — Data Manipulation](https://www.postgresql.org/docs/18/dml.html)
- [Microsoft — Transact-SQL statements](https://learn.microsoft.com/sql/t-sql/statements/statements)
