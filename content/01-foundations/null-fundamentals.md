---
schema_version: 1
id: DBKB-FND-0016
title: NULL Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [sql, data-modeling]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0002, DBKB-FND-0006]
related: [DBKB-FND-0011, DBKB-FND-0012, DBKB-FND-0017, DBKB-FND-0024]
aliases: ["NULL", null marker, missing value]
search_keywords: ["NULL", unknown, missing, IS NULL, COALESCE, COUNT]
risk: safe
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0001]
source_ids: [SRC-000004, SRC-000005]
acceptance_criteria:
  - Elmagyarázza, hogy a NULL marker nem nulla és nem üres string.
  - Bemutatja az IS NULL, comparison és aggregate alapviselkedést.
  - A portable állításokat execution-verified példával támasztja alá.
---
# NULL Fundamentals

A SQL `NULL` egy marker arra, hogy az adott helyen nincs ismert, alkalmazható érték. Nem
számérték, nem üres string és nem a nulla speciális írásmódja. A pontos üzleti jelentést a
schema és a data contract adja: lehet „még nem ismert”, „nem alkalmazható” vagy „nem érkezett
meg”. Ha ezek a jelentések üzletileg különböznek, egyetlen nullable column gyakran túl kevés
információt hordoz.

## Mi nem a NULL?

```text
NULL ≠ 0
NULL ≠ ''
NULL ≠ false
NULL ≠ 'NULL'
```

Az üres string ismert, nulla hosszúságú text. A `0` ismert szám. A `false` ismert boolean
érték. A `'NULL'` öt karakterből álló text. Vendor behavior eltérhet bizonyos coercion vagy
legacy beállítások esetén, ezért ingestionkor explicit contract szükséges.

## Tesztelés

`NULL` jelenlétét `IS NULL`, hiányát `IS NOT NULL` predicate-tel vizsgáld:

```sql
SELECT customer_code
FROM customer
WHERE phone_number IS NULL;
```

Az `expression = NULL` nem helyes null-teszt. A PostgreSQL 18 official comparison
dokumentációja szerint az ordinary comparison operator `NULL` input mellett `NULL`
(unknown) eredményt ad, és explicit `IS NULL`/`IS NOT NULL` használatot ír le. Null-safe
equalityre létezhet `IS [NOT] DISTINCT FROM` vagy vendor-specifikus alternatíva, de ezek
portability-jét külön kell vizsgálni.

## Three-valued logic hatása

A comparison eredménye lehet `TRUE`, `FALSE` vagy `UNKNOWN`. A `WHERE` csak azokat a row-kat
tartja meg, amelyekre a predicate `TRUE`; a `FALSE` és `UNKNOWN` row kiesik. Ezért:

```sql
WHERE country_code <> 'HU'
```

nem tartja meg azokat a row-kat, ahol `country_code IS NULL`. Ha az üzleti követelmény az,
hogy „nem magyar vagy ismeretlen”, ezt explicit kell leírni:

```sql
WHERE country_code <> 'HU' OR country_code IS NULL
```

A teljes truth table és a `NOT`, `AND`, `OR` következményei a DBKB-FND-0017 dokumentum
témája. A PostgreSQL 18 official logical-operator oldala explicit true/false/null truth
table-t közöl.

## Aggregate viselkedés

A legtöbb aggregate a `NULL` inputot kihagyja, de a `COUNT(*)` row-kat számol. Emiatt a két
számlálás eltérhet:

```sql
SELECT COUNT(phone_number), COUNT(*)
FROM customer;
```

Ha két row közül az egyik `phone_number` értéke `NULL`, akkor a fenti portable példában az
első eredmény `1`, a második `2`. A `SQL-FND-0002` példa ezt izolált SQLite környezetben
ténylegesen futtatja és expected resulttal ellenőrzi. Ez az evidence a deklarált
portable/SQLite szemantikára vonatkozik, nem bizonyít minden engine minden edge case-ére.

## Constraint és modeling

A `NOT NULL` azt mondja ki, hogy a marker nem megengedett. Nem garantálja, hogy a value
helyes, nem üres, üzletileg létező vagy időszerű. Ehhez type, `CHECK`, `UNIQUE`, foreign key
vagy application/data-quality rule szükséges.

Nullable column tervezésekor kérdezd meg:

- Valóban hiányozhat az érték?
- A „unknown” és „not applicable” ugyanazt jelenti?
- Később kötelezővé válhat-e?
- Hogyan viselkedik sorting, grouping, uniqueness és join során?
- A downstream consumer felismeri-e a hiányt, vagy default value-ra cseréli?

## `COALESCE` óvatos használata

A `COALESCE(a, b, ...)` az első nem-NULL expressiont adja vissza. Hasznos presentation vagy
fallback esetén, de a túl korai defaultolás információt veszít:

```sql
SELECT COALESCE(phone_number, 'nincs megadva')
FROM customer;
```

A resultban már nem különíthető el, hogy a forrás valóban a `nincs megadva` textet tartalmazta,
vagy a query helyettesített. Calculation esetén a `COALESCE(amount, 0)` csak akkor helyes, ha
az üzleti contract szerint a missing amount valóban nullával ekvivalens.

## Gyakori hibák

- `= NULL` vagy `<> NULL` használata.
- Nullable operandus miatt kieső row-k figyelmen kívül hagyása.
- `COUNT(column)` és `COUNT(*)` összekeverése.
- Missing value automatikus nullára vagy üres stringre cserélése.
- Minden hiányjelentés egyetlen markerbe sűrítése.

## Források

- [PostgreSQL 18 — Comparison Functions and Operators](https://www.postgresql.org/docs/18/functions-comparison.html) — comparison, `IS NULL`, `IS DISTINCT FROM` és unknown viselkedés.
- [PostgreSQL 18 — Logical Operators](https://www.postgresql.org/docs/18/functions-logical.html) — SQL three-valued logic truth table.
