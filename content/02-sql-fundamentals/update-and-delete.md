---
schema_version: 1
id: DBKB-SQL-0021
title: UPDATE and DELETE
type: concept
primary_domain: sql-fundamentals
secondary_domains: [data-integrity, operations]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0006, DBKB-SQL-0020]
related: [DBKB-FND-0024, DBKB-SQL-0022]
aliases: [row modification, row deletion]
search_keywords: [update, delete, where, transaction, rollback]
risk: destructive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000031, SRC-000030]
acceptance_criteria:
  - Bemutatja az UPDATE és DELETE scope-ját.
  - Kötelező safety workflow-t ad broad modification ellen.
  - Izolált környezetben futtatott végállapot-példát ad.
---
# UPDATE and DELETE

Az `UPDATE` meglévő sorok columnértékeit módosítja, a `DELETE` sorokat távolít el. Mindkettő `WHERE`
nélkül az összes target sort érintheti; ez syntactically valid, de productionben destructive.

```sql
UPDATE customer
SET status = 'INACTIVE'
WHERE customer_id = 101;

DELETE FROM customer
WHERE customer_id = 101;
```

## Kötelező safety workflow

1. Ugyanazzal a predicate-tel futtass `SELECT` preview-t és rögzíts expected countot.
2. Ellenőrizd a backup/recovery és referential action következményeket.
3. Használj explicit transactiont, ha az engine és operation támogatja.
4. Ellenőrizd az affected row countot és a postconditiont commit előtt.
5. Production runhoz peer review, change window és rollback plan szükséges.

Concurrent változás miatt a preview és modification között eltérhet a target set; megfelelő isolation,
locking vagy optimistic version predicate kellhet. Join-alapú update/delete syntax és modified-row
returning vendorfüggő.

A `SQL-SQL-0021` kizárólag ephemeral SQLite adatbázist módosít: targeted update és delete után exact
végállapotot ellenőriz. A példa `destructive: true`, ezért a harness csak explicit
`--allow-destructive` flaggel futtatja.

## Források

- [PostgreSQL 18 — Data Manipulation](https://www.postgresql.org/docs/18/dml.html)
- [Microsoft — Transact-SQL statements](https://learn.microsoft.com/sql/t-sql/statements/statements)
