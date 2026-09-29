---
schema_version: 1
id: DBKB-SQL-0007
title: Predicates and Comparison Logic
type: concept
primary_domain: sql-fundamentals
secondary_domains: [foundations]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0006, DBKB-FND-0017]
related: [DBKB-SQL-0010, DBKB-SQL-0011]
aliases: [comparison predicate, three-valued logic]
search_keywords: [equals, between, in, like, "null", unknown]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000022, SRC-000024]
acceptance_criteria:
  - Rendszerezi az alap comparison predicate-eket.
  - Bemutatja a three-valued logic következményét.
  - Futtatható NULL példát ad.
---
# Predicates and Comparison Logic

Predicate-ek közé tartozik az equality és ordering comparison, `BETWEEN`, `IN`, pattern matching,
existence és nullness vizsgálat. Operandjaik type compatibilityje és collationje befolyásolja az
eredményt. Text összehasonlításnál ne feltételezz binary vagy case-insensitive semanticset a
deklarált collation nélkül.

SQL-ben a `NULL` nem egy „üres érték”, hanem hiányzó vagy ismeretlen jelölés. A `NULL`-lal végzett
legtöbb comparison `UNKNOWN` lesz. A `NOT` sem változtatja ezt automatikusan `TRUE`-vá; ezért a
nullable inputot minden truth table-ben külön ágnak kell tekinteni.

## Gyakori csapdák

- `column = NULL` helyett `column IS NULL` szükséges.
- `NOT IN` nullable listával vagy subqueryvel meglepő `UNKNOWN` eredményt adhat; az input nullabilityt
  bizonyítani vagy más formulationt választani kell.
- `BETWEEN` mindkét határt tartalmazza; timestamp napokra gyakran jobb a fél-nyílt range.
- `LIKE` wildcard és escape szabálya, valamint case behavior dialect- és collationfüggő.
- Floating-point equality üzleti pontosságot ritkán fejez ki jól.

A `SQL-SQL-0007` futtatás igazolja, hogy `value = NULL` nem választ sort, míg `IS NULL` igen az
SQLite környezetben. Ez a példa a portable three-valued logic magot célozza, nem általánosít minden
vendor-specific comparison operatorra.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [PostgreSQL 18 Tutorial — Querying a Table](https://www.postgresql.org/docs/18/tutorial-select.html)
