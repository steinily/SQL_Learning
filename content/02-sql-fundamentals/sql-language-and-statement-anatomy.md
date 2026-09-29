---
schema_version: 1
id: DBKB-SQL-0002
title: SQL Language and Statement Anatomy
type: concept
primary_domain: sql-fundamentals
secondary_domains: [foundations]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver]
sql_dialects: [portable-sql, postgresql, tsql]
scope: cross-vendor
prerequisites: [DBKB-SQL-0001]
related: [DBKB-SQL-0003, DBKB-SQL-0004, DBKB-SQL-0006, DBKB-SQL-0008]
aliases: [statement anatomy, query clauses]
search_keywords: [statement, clause, expression, predicate, identifier, literal]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000022, SRC-000028]
acceptance_criteria:
  - Megkülönbözteti a statement, clause, expression és predicate fogalmát.
  - Bemutatja a SELECT fő clause-ait és logical szerepüket.
  - Felhívja a figyelmet a lexical és dialect különbségekre.
---
# SQL Language and Statement Anatomy

A **statement** teljes SQL utasítás. Clause-okból épül fel; a clause-on belül expression számít
értéket, a predicate pedig `TRUE`, `FALSE` vagy `UNKNOWN` logikai eredményt adhat. Identifier nevez
meg objectet vagy columnt, literal pedig közvetlen értéket jelöl. Parameter a literal biztonságos,
typed helyettesítője lehet client API-n keresztül.

## Egy query részei

A gyakori írott sorrend: `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, majd
dialect-specifikus row limiting. Ez nem azonos sem a fogalmi feldolgozási modellel, sem a physical
plan sorrendjével. Például a `WHERE` input sorokat szűr, míg a `HAVING` már groupokat.

Az alias visibility ezért nem vezethető le egyszerűen a statement balról jobbra olvasásából.
Ha egy alias egy másik clause-ban használható, azt az adott dialect dokumentációja határozza meg.

## Lexical szabályok

Keyword, identifier, string literal, numeric literal, operator és comment alkotja a szöveget.
Quoted identifier és string literal idézőjele nem cserélhető fel. Case folding, reserved word lista,
identifier length és parameter marker vendorfüggő. Dynamic SQL építésénél value-t parameterként kell
átadni; object nevet csak allowlist és dialect-helyes quoting után szabad beilleszteni.

## Review kérdések

Ellenőrizd, hogy minden column reference egyértelmű-e, a predicate kezeli-e a `NULL` lehetőségét,
a row order explicit-e, és a statement módosít-e adatot. A semicolon használata jó statement
boundary; egyes eszközök batch separatora nem része az SQL statementnek.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
