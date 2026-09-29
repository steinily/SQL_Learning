---
schema_version: 1
id: DBKB-SQL-0010
title: Expressions and Operators
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
prerequisites: [DBKB-SQL-0005, DBKB-FND-0012]
related: [DBKB-SQL-0007, DBKB-SQL-0011]
aliases: [scalar expression, operator]
search_keywords: [arithmetic, concatenation, case, coalesce, precedence]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000024, SRC-000028]
acceptance_criteria:
  - Bemutatja az expression compositiont és operator precedence-et.
  - Tárgyalja a type és NULL hatását.
  - Futtatható CASE példát ad.
---
# Expressions and Operators

Expression literalból, column reference-ből, operatorból, functionből és más expressionökből épül.
Arithmetic, comparison, boolean és text műveletek jelentése az operand type-jától függ; az azonos
jelölés sem feltétlen azonos minden dialectben.

`CASE` explicit conditional expressiont ad. `COALESCE` az első nem-`NULL` értéket választja, de az
argumentumok compatible result type-ja továbbra is szükséges. A legtöbb arithmetic művelet `NULL`
input esetén `NULL` eredményt ad; ez nem helyettesíti a business default tudatos megadását.

```sql
SELECT quantity,
       CASE WHEN quantity >= 10 THEN 'bulk' ELSE 'standard' END AS band
FROM order_line;
```

## Precedence és overflow

Zárójelekkel dokumentáld a kívánt groupingot, különösen boolean expressionnél. Integer division,
numeric promotion, overflow, string concatenation és modulo részletei vendor- és type-specifikusak.
Pénzügyi számításhoz explicit exact numeric type és rounding policy kell.

Function alkalmazása indexed columnra vagy implicit conversion performance hatású lehet, de a
konkrét access pathot csak execution plan bizonyítja. Correctness review során előbb a domain,
`NULL`, boundary és error case-eket vizsgáld.

A `SQL-SQL-0010` example arithmetic és `CASE` outputot ellenőriz SQLite-on.

## Források

- [PostgreSQL 18 Tutorial — Querying a Table](https://www.postgresql.org/docs/18/tutorial-select.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
