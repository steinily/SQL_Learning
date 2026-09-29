---
schema_version: 1
id: DBKB-FND-0015
title: Date and Time Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [sql, data-modeling]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-FND-0012]
related: [DBKB-FND-0025, DBKB-FND-0031]
aliases: [date, time, timestamp, interval, time zone]
search_keywords: [UTC, offset, civil time, daylight saving, temporal]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0003]
source_ids: [SRC-000013]
acceptance_criteria:
  - Elkülöníti a date, local time, instant, duration és interval fogalmát.
  - Bemutatja az offset és named time zone különbségét.
  - Figyelmeztet a parsing, DST és inclusive boundary hibákra.
---
# Date and Time Fundamentals

Temporal adatnál előbb a jelentést kell rögzíteni. Egy **date** calendar nap, egy **local
date-time** falióra szerinti időpont zone nélkül, egy **instant** az idővonal egy pontja, egy
**duration** eltelt idő, míg egy calendar **interval** month/day összetevői nem mindig
válthatók fix másodpercre.

## Offset és time zone

A UTC offset, például `+02:00`, csak egy adott eltérést közöl. A named time zone, például
`Europe/Budapest`, történeti és jövőbeli daylight-saving szabályokat hordozhat. Ugyanazon zone
offsetje időponttól függhet; ugyanaz a local time DST átálláskor lehet ambiguous vagy nem létező.

## Tárolási döntés

- Esemény instantjához tárolj zone-aware instantot/UTC-normalized value-t, és szükség esetén
  az eredeti zone/contextet.
- Születésnap vagy üzleti nap nem instant; `date` megfelelőbb.
- „Minden nap 09:00 Budapesten” recurring civil-time rule, nem egyetlen UTC time.
- Duration és calendar period ne legyen automatikusan felcserélve.

PostgreSQL 18 külön `date`, `time`, `timestamp` és `interval` type-okat dokumentál; input
értelmezését `DateStyle` és time-zone context is befolyásolhatja. Cross-vendor migrationnél a
névazonosság nem bizonyít azonos semanticsot.

## Query boundary

Időintervallumra a half-open `[start, end)` forma csökkenti az átfedést és fractional-second
precision problémát:

```sql
WHERE occurred_at >= :day_start
  AND occurred_at <  :next_day_start
```

A boundary értékeket ugyanabban az instant/zone semanticsban képezd, mint a stored data.

## Clock és audit

Az event time, ingestion time, processing time és database commit time külön fogalom. Clock
skew és retry miatt egyik sem garantál automatikus total ordert distributed rendszerben.
Auditnál nevezd meg, melyik időt rögzíted és ki adta.

## Forrás

- [PostgreSQL 18 — Date/Time Types](https://www.postgresql.org/docs/18/datatype-datetime.html)
