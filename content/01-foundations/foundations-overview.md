---
schema_version: 1
id: DBKB-FND-0001
title: Foundations Overview
type: overview
primary_domain: foundations
secondary_domains: [sql, database-engineering, data-engineering]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: []
scope: general
prerequisites: []
related: [DBKB-FND-0002, DBKB-FND-0003, DBKB-FND-0006, DBKB-FND-0025, DBKB-FND-0031]
aliases: [foundations, alapok]
search_keywords: [data, database, relational, transaction, workload, learning path]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0001, RP-FND-0002, RP-FND-0003, RP-FND-0004]
source_ids: [SRC-000001, SRC-000002, SRC-000003]
acceptance_criteria:
  - Navigációt ad az M01 canonical fogalmaihoz.
  - Megmutatja a tanulási sorrendet és a fogalmi határokat.
  - Nem duplikálja a részletes canonical dokumentumokat.
---
# Foundations Overview

Ez a modul a Data & Database Engineering közös szókészletét és gondolkodási keretét adja.
Nem egyetlen vendor termékének bevezetője: azt rögzíti, mit jelent data, database, relation,
integrity, transaction, consistency és workload, mielőtt a későbbi modulok SQL syntaxra,
engine behaviorre vagy operációra térnek át.

## Ajánlott tanulási sorrend

1. [Data Fundamentals](data-fundamentals.md) és [Database Fundamentals](database-fundamentals.md)
   választja szét a jelentést, reprezentációt, repositoryt és kezelő rendszert.
2. [Database Models](database-models.md), [Relational Model Fundamentals](relational-model-fundamentals.md)
   és [Tables Rows and Columns](tables-rows-and-columns.md) építi fel a logical modelt.
3. [Database Keys](database-keys.md), [Relationships](relationships.md),
   [Referential Integrity](referential-integrity.md) és [Constraints](constraints.md) mutatja meg,
   hogyan lesz az üzleti szabályból deklarált integrity.
4. [Data Types](data-types.md), [NULL Fundamentals](null-fundamentals.md) és
   [Three-Valued Logic](three-valued-logic.md) tisztázza az értékek és predicate-ek viselkedését.
5. [Relational Algebra Fundamentals](relational-algebra-fundamentals.md) és
   [Set-Based Thinking](set-based-thinking.md) készít fel a declarative SQL-re.
6. [Transaction Fundamentals](transaction-fundamentals.md), [ACID](acid.md),
   [Concurrency Fundamentals](concurrency-fundamentals.md), [Consistency Models](consistency-models.md)
   és [CAP Theorem Fundamentals](cap-theorem-fundamentals.md) választja szét a transaction és
   distributed-system guarantee-kat.
7. [OLTP vs OLAP](oltp-vs-olap.md), [Database Workloads](database-workloads.md) és
   [Database Warehouse Lake and Lakehouse](database-warehouse-lake-and-lakehouse.md) kapcsolja
   a fogalmakat architecture választásokhoz.

## Három megkülönböztetés

**Logical és physical:** a schema, key és relation a jelentés és szerkezet felől közelít; a
page, file, index és execution plan a megvalósítás felől. Kapcsolódnak, de nem cserélhetők fel.

**Guarantee és mechanizmus:** az atomicity, isolation vagy referential integrity elvárt
viselkedés. Lock, MVCC, log vagy constraint egy lehetséges mechanizmus. Ugyanazt a guarantee-t
eltérő mechanizmusok adhatják, és ugyanaz a mechanizmus configurationtől függően eltérő
eredményt adhat.

**General concept és vendor behavior:** a canonical elmélet itt kap helyet; a PostgreSQL,
SQL Server és MySQL részletek saját technology dokumentumokban jelennek meg. A PostgreSQL 18
official dokumentáció ebben a modulban concrete, version-pinned példaforrás, nem univerzális
SQL-standard helyettesítő.

## Hogyan használd a modult?

Minden dokumentum elején ellenőrizd a prerequisites listát. A runnable példák külön execution
evidence rekorddal rendelkeznek; `execution-verified` csak tényleges futás után jelenhet meg.
A források claim-level research package-ekhez kötöttek. Ha egy állítás scope-ja vagy versionje
nem igazolható, a helyes eredmény `VERIFY_REQUIRED`, nem találgatás.

## Források

- [NIST CSRC — Database](https://csrc.nist.gov/glossary/term/Database)
- [IBM Research — Codd relational-model paper](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks)
- [PostgreSQL 18 — SQL Concepts](https://www.postgresql.org/docs/18/tutorial-concepts.html)
