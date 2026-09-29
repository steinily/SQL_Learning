---
schema_version: 1
id: DBKB-ASQL-0017
title: LATERAL and APPLY
type: comparison
primary_domain: advanced-sql
secondary_domains: [sqlserver, postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver]
sql_dialects: [postgresql, tsql]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0012, DBKB-ISQL-0023]
related: [DBKB-ASQL-0012]
aliases: [correlated table expression, cross apply, outer apply]
search_keywords: [lateral, cross apply, outer apply, correlated from]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0002]
source_ids: [SRC-000036, SRC-000029]
acceptance_criteria:
  - PostgreSQL LATERAL és T-SQL APPLY scope-ot különít el.
  - Bemutatja a per-left-row correlated table resultot.
  - Nem állít cross-vendor syntax equivalenciát.
---
# LATERAL and APPLY

PostgreSQL `LATERAL` lehetővé teszi, hogy egy `FROM` item korábban felsorolt item columnjaira
hivatkozzon. T-SQL `CROSS APPLY` és `OUTER APPLY` hasonló correlated table-source use case-eket fed,
de syntaxuk és teljes semanticsük nem azonosítható automatikusan.

Tipikus minta a customerenkénti top-N related row vagy parameterized set-returning function. Inner-like
forma csak outputot ad, ha a correlated source sort termel; outer-like forma a bal sort üres jobb oldal
mellett is megőrizheti.

Correlation nem bizonyít soronkénti physical executiont. Index és plan fontos lehet, de mérés kell.
Row limitinghez deterministic order szükséges. A local SQLite környezet nem a PostgreSQL/T-SQL
syntax validátora, ezért ez a comparison source-verified, execution `N/A`.

## Források

- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
- [Microsoft — FROM clause plus JOIN, APPLY, PIVOT](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver17)
