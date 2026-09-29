---
schema_version: 1
id: DBKB-SQL-0022
title: DDL Fundamentals
type: concept
primary_domain: sql-fundamentals
secondary_domains: [data-modeling, operations]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0001, DBKB-FND-0010]
related: [DBKB-SQL-0020, DBKB-SQL-0021, DBKB-FND-0024]
aliases: [data definition language, schema definition]
search_keywords: [create, alter, drop, table, constraint, migration]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000030, SRC-000009]
acceptance_criteria:
  - Elhelyezi a CREATE ALTER DROP műveleteket a DDL-ben.
  - Bemutatja a migration és rollback felelősségeket.
  - Ephemeral környezetben futtatott CREATE TABLE példát ad.
---
# DDL Fundamentals

A DDL schema objecteket definiál és változtat. Gyakori statementek a `CREATE`, `ALTER` és `DROP`;
table, constraint, index, view és más object syntaxa termék- és verziófüggő. A DDL nem egyszerűen
„admin SQL”: application compatibilityt, lockingot, storage-ot és recoveryt érinthet.

```sql
CREATE TABLE customer (
  customer_id INTEGER PRIMARY KEY,
  customer_name VARCHAR(200) NOT NULL
);
```

## Migration discipline

Schema változást versioned, review-olt migrationként kezelj. Dokumentáld a preconditiont,
postconditiont, backward/forward compatibilityt, lock és runtime kockázatot, adat-backfillt, valamint
a recovery utat. A „rollback” nem mindig inverse DDL: adatvesztő `DROP COLUMN` után csak backup vagy
külön megőrzött adat segíthet.

Transactional DDL behavior, online operation és `IF EXISTS/IF NOT EXISTS` support eltér. Ezeket az
adott engine official dokumentációja és staging rehearsal alapján kell megállapítani. Production
execution resultot local syntax checkből nem szabad következtetni.

Constraintet lehetőleg a schemában fejezz ki, mert minden writerre érvényes; ugyanakkor meglévő dirty
data, validation timing és deployment ordering miatt külön rollout terv kell.

A `SQL-SQL-0022` csak ephemeral SQLite adatbázisban hoz létre constrained table-t és ellenőrzi a
schema működését. Nem igazolja más engine online vagy transactional DDL tulajdonságait.

## Források

- [Microsoft — Transact-SQL statements](https://learn.microsoft.com/sql/t-sql/statements/statements)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
