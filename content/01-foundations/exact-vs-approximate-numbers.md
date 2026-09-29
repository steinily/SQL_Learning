---
schema_version: 1
id: DBKB-FND-0013
title: Exact vs Approximate Numbers
type: concept
primary_domain: foundations
secondary_domains: [sql, data-quality]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0012]
related: [DBKB-FND-0024, DBKB-FND-0031]
aliases: [decimal vs float, exact numeric, approximate numeric]
search_keywords: [numeric, decimal, real, double precision, rounding, precision, scale]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0003]
source_ids: [SRC-000010]
acceptance_criteria:
  - Elkülöníti az exact decimal/integer és approximate floating-point típust.
  - Megmagyarázza a precision, scale, rounding és equality kockázatot.
  - Tényleges floating-point demonstrációt kapcsol a dokumentumhoz.
---
# Exact vs Approximate Numbers

Az **exact numeric** type a támogatott tartományon belül pontos egész vagy decimal értéket
reprezentál. Az **approximate numeric** type tipikusan IEEE 754 binary floating-point, ahol
egyes decimal törtek csak közelítően tárolhatók.

PostgreSQL 18 official dokumentációban az `integer` family és a `numeric`/`decimal` exact,
míg a `real` és `double precision` inexact. A konkrét range, special value és rounding behavior
version- és platformfüggő lehet.

## Precision és scale

A decimal **precision** az összes significant digit száma, a **scale** a fractional digit
száma. `NUMERIC(12,2)` tipikusan legfeljebb tíz egész és két fractional digitre ad contractot.
Input scale-túllépésnél rounding történhet, range-túllépésnél error; pontos szabályt az engine
dokumentációjából ellenőrizd.

## Mikor melyik?

- Pénzügyi amount, adó, könyvelési quantity: exact decimal vagy integer minor unit.
- Count és identifier: megfelelő range-ű integer.
- Szenzor, tudományos számítás, nagy dinamikatartomány: floating point lehet megfelelő, ha az
  error tolerance deklarált.

Floating point esetén közvetlen equality helyett domainfüggő tolerance vagy interval kellhet.
Az abszolút és relatív tolerance választása a magnitude-tól és követelménytől függ; nincs
univerzális epsilon.

## Demonstráció

A `SQL-FND-0007` SQLite környezetben ténylegesen futtatja a `0.1 + 0.2 = 0.3` comparisont,
amely `0`/false eredményt ad az ott használt binary floating representation miatt. Ez egy
konkrét demonstráció, nem általános benchmark és nem bizonyít minden numeric type-ra.

## Aggregate és conversion

Sok közelítő value összege error accumulationt mutathat. Decimal–float implicit conversion
megváltoztathatja az expression result type-ját. API boundaryn ellenőrizd a client language
mappinget is: egy database decimal nem feltétlenül marad decimal, ha JSON numberen vagy binary
float propertyn halad át.

## Forrás

- [PostgreSQL 18 — Numeric Types](https://www.postgresql.org/docs/18/datatype-numeric.html)
