---
schema_version: 1
id: DBKB-FND-0012
title: Data Types
type: concept
primary_domain: foundations
secondary_domains: [sql, data-modeling]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-FND-0007]
related: [DBKB-FND-0011, DBKB-FND-0013, DBKB-FND-0014, DBKB-FND-0015, DBKB-FND-0016]
aliases: [type, domain, SQL data type]
search_keywords: [integer, decimal, text, boolean, date, timestamp, binary]
risk: safe
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0003]
source_ids: [SRC-000010, SRC-000011, SRC-000013]
acceptance_criteria:
  - Elmagyarázza a type representation, operation és constraint szerepét.
  - Bemutatja a fő type family-ket és portability kockázatukat.
  - Elválasztja a physical type-ot a business domaintől.
---
# Data Types

A **data type** meghatározza egy value lehetséges representationjét, értéktartományát és az
értelmezhető operationök egy részét. A type segít megakadályozni értelmetlen state-eket, de nem
teljes business model: az `INTEGER` nem mondja meg, hogy a quantity pozitív, a `VARCHAR(2)` nem
bizonyítja, hogy létező country code.

## Fő type family-k

- **Exact numeric:** integer és decimal/numeric; pénzhez és darabszámhoz gyakran szükséges.
- **Approximate numeric:** binary floating point; méréshez és tudományos számításhoz hasznos,
  de equality és rounding külön figyelmet igényel.
- **Character:** fixed vagy variable length text, encoding és collation kontextussal.
- **Boolean:** true/false, nullable esetben unknown állapottal együtt.
- **Temporal:** date, time, timestamp és interval; time-zone semantics nélkül félreérthető.
- **Binary:** byte sequence, amelyre text encoding szabály nem alkalmazható automatikusan.
- **Structured/vendor types:** array, JSON, XML, range, spatial vagy domain type; portability
  és indexability engine-specifikus.

## Type-választás

Előbb a jelentést nevezd meg, majd a szükséges range-et, precisiont és operationöket. Kerüld a
„mindent textként” mintát: késői parsinget, gyenge constraintet és bizonytalan sortingot okoz.
Ugyanakkor indokolatlanul szűk type se legyen: range overflow és migration lehet az eredmény.

Type conversion lehet explicit `CAST`, implicit coercion vagy client-driver mapping. Az
implicit conversion correctnesset és index használatot is befolyásolhat; vendor rules nélkül
ne feltételezd az eredményt.

## Domain és constraint

A business domainet type plusz constraint együtt közelíti:

```sql
quantity INTEGER NOT NULL CHECK (quantity > 0)
```

Ha több column ugyanazt a domain rule-t használja, reusable domain/type vagy central reference
table lehet megfelelő, de feature availability vendorfüggő.

## Portability

Az azonos type name eltérő range, storage, rounding, collation vagy timezone behavior mögött
állhat. Migrationnél a source és target official dokumentációját, boundary value-okat és
round-trip teszteket együtt használd.

## Források

- [PostgreSQL 18 — Numeric Types](https://www.postgresql.org/docs/18/datatype-numeric.html)
- [PostgreSQL 18 — Character Types](https://www.postgresql.org/docs/18/datatype-character.html)
- [PostgreSQL 18 — Date/Time Types](https://www.postgresql.org/docs/18/datatype-datetime.html)
