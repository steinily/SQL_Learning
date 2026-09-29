---
schema_version: 1
id: DBKB-FND-0034
title: Database Abstraction Layers
type: concept
primary_domain: foundations
secondary_domains: [application-engineering, sql]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [python-db-api, jdbc]
sql_dialects: []
scope: general
prerequisites: [DBKB-FND-0003]
related: [DBKB-FND-0012, DBKB-FND-0025, DBKB-FND-0035]
aliases: [driver, database API, ORM, query builder]
search_keywords: [connection, cursor, parameter binding, object relational mapping]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-FND-0004]
source_ids: [SRC-000021]
acceptance_criteria:
  - Elkülöníti a protocol/driver, API, query builder és ORM réteget.
  - Megmutatja, mely database semantics nem tűnik el az abstraction mögött.
  - Kiemeli a parameter binding és transaction ownership fontosságát.
---
# Database Abstraction Layers

Database abstraction layer egységesebb application interface-t ad connection, execution,
result mapping vagy object persistence számára. Csökkentheti a boilerplate-et, de nem törli el
a database type, transaction, concurrency és performance semanticsát.

## Rétegek

- **Wire protocol/driver:** bytes, authentication és vendor protocol.
- **Database API:** connection, cursor/command, parameter és result contract. PEP 249 például
  közös Python DB-API 2.0 interface-t definiál.
- **Query builder:** code-ból statementet épít, gyakran parameter bindinggel.
- **ORM:** object state-et table/row state-re képez, identity map és unit-of-work viselkedéssel.
- **Repository/service layer:** domain-specific boundaryt ad az alkalmazásnak.

## Nem absztrahálható el teljesen

Isolation level, lock duration, null handling, collation, generated key, affected-row semantics,
bulk behavior és vendor SQL továbbra is hat. „Database agnostic” claimet minden supported engine
ellen contract teszttel kell igazolni.

## Parameter binding

Value-t ne string concatenationnel illessz SQL-be. A driver parameter API-ja kezeli a value
boundaryt és csökkenti az SQL injection kockázatot. Identifier vagy keyword általában nem value
parameter; allowlist és dialect-aware quoting kell.

## Transaction ownership

Legyen egyértelmű, mely réteg nyit, commitol és rollbackel. Hidden lazy load transactionön kívül
vagy implicit flush váratlan queryt és lockot okozhat. Observabilityben a generated SQL,
parameter shape és transaction boundary legyen hozzáférhető érzékeny value-k kiszivárogtatása
nélkül.

## Forrás

- [PEP 249 — Python Database API Specification v2.0](https://peps.python.org/pep-0249/)
