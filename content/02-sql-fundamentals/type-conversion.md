---
schema_version: 1
id: DBKB-SQL-0011
title: Type Conversion
type: concept
primary_domain: sql-fundamentals
secondary_domains: [foundations, data-quality]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0012, DBKB-SQL-0010]
related: [DBKB-SQL-0007, DBKB-FND-0014, DBKB-FND-0015]
aliases: [cast, coercion, convert]
search_keywords: [cast, convert, implicit conversion, precision, truncation]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQL-0001]
source_ids: [SRC-000022, SRC-000028]
acceptance_criteria:
  - Megkülönbözteti az explicit és implicit conversiont.
  - Bemutatja a correctness és portability kockázatokat.
  - Futtatható CAST példát ad.
---
# Type Conversion

Type conversion egy értéket más target type representationjébe helyez. A standard jellegű explicit
forma `CAST(expression AS type)`; vendorok további functionöket és type neveket adnak. Implicit
conversiont az engine végezhet comparison, arithmetic, assignment vagy function binding során.

```sql
SELECT CAST('42' AS INTEGER) AS parsed_value;
```

Az explicit conversion láthatóvá teszi a szándékot, de nem teszi automatikusan portable-lé a type
nevet, accepted input formatot vagy failure behavior-t. Invalid text egy engine-en error, más
contextben special value vagy más eredmény lehet; ezt official documentation és execution test
nélkül nem szabad feltételezni.

## Loss és ambiguity

Narrowing conversion overflow-t, truncationt vagy roundingot okozhat. Approximate és exact numeric
közötti átmenet precisiont veszíthet. Text–date conversionnél explicit, unambiguous format és timezone
policy kell. Character conversionnél encoding és collation is része a jelentésnek.

Implicit conversion a comparison melyik oldalán történik, hatással lehet correctnessre és index
használatra. Data ingestionnél különítsd el a raw textet, validationt és typed targetet; a sikertelen
rekordot ne alakítsd csendben business defaulttá.

A `SQL-SQL-0011` SQLite-on egy jól definiált integer castot ellenőriz. Ez nem bizonyítja PostgreSQL
vagy T-SQL invalid-input és range szabályait.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [Microsoft — SELECT (Transact-SQL)](https://learn.microsoft.com/sql/t-sql/queries/select-transact-sql/)
