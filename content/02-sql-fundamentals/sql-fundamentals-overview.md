---
schema_version: 1
id: DBKB-SQL-0001
title: SQL Fundamentals Overview
type: overview
primary_domain: sql-fundamentals
secondary_domains: [foundations, data-modeling]
levels: [beginner]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0001, DBKB-FND-0004]
related: [DBKB-SQL-0002, DBKB-SQL-0003, DBKB-SQL-0016, DBKB-SQL-0022]
aliases: [SQL basics, query fundamentals]
search_keywords: [select, from, where, group by, order by, dml, ddl]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0001, RP-SQL-0002]
source_ids: [SRC-000022, SRC-000028, SRC-000030, SRC-000031]
acceptance_criteria:
  - Elhelyezi a query, DML és DDL területeket az SQL nyelvben.
  - Elkülöníti a declarative eredményigényt a physical executiontől.
  - Kijelöli a portability és safety alapelveket.
---
# SQL Fundamentals Overview

Az **SQL** relációs adatok definíciójára, lekérdezésére és módosítására használt nyelvcsalád.
Declarative megközelítésében a statement elsősorban a kívánt eredményt vagy state-változást írja
le; a physical access path, join algorithm és operator scheduling az engine feladata. A nyelvnek
van szabványos magja, de a production dialect mindig konkrét termékhez és verzióhoz kötött.

## Alapterületek

- A query `SELECT`-tel projectiont, table source-ot, filteringet, groupingot és orderinget ad meg.
- A DML `INSERT`, `UPDATE` és `DELETE` műveletekkel sorokat változtat.
- A DDL például `CREATE`, `ALTER` és `DROP` statementekkel schema objecteket kezel.
- A transaction control és access control külön felelősségi kör; későbbi modulok részletezik.

Ezek a kategóriák hasznos tanulási határok, nem minden vendor teljes taxonómiája. A syntax support,
implicit conversion, `NULL` ordering, row limiting és módosított sorok visszaadása eltérhet.

## Gondolkodási modell

Egy query olvasásakor különítsd el a result shape-et, a source row-kat, a row-level filtert, a
group-level filtert és a végső ordert. A leírt clause order nem a physical execution ígérete.
Correctnesshez explicit join condition, megfelelő type és deterministic `ORDER BY` szükséges;
performance következtetéshez execution plan és mérés kell.

## Biztonság és ellenőrzés

Adatmódosítás előtt ugyanazzal a predicate-tel futtatott `SELECT`, explicit transaction, backup és
row-count ellenőrzés csökkenti a kockázatot. Példát csak a deklarált engine-en futtatott evidence
alapján nevezünk execution-verifiednek. Az itt bemutatott portable subset SQLite-on fut; a
PostgreSQL és T-SQL eltérések official dokumentációból source-verifiedek.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
- [Microsoft — Transact-SQL statements](https://learn.microsoft.com/sql/t-sql/statements/statements)
- [PostgreSQL 18 — Data Manipulation](https://www.postgresql.org/docs/18/dml.html)
