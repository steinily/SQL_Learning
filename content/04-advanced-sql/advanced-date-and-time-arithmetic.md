---
schema_version: 1
id: DBKB-ASQL-0020
title: Advanced Date and Time Arithmetic
type: concept
primary_domain: advanced-sql
secondary_domains: [temporal-data]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0015]
related: [DBKB-ASQL-0007, DBKB-ASQL-0021]
aliases: [temporal arithmetic]
search_keywords: [timestamp, interval, timezone, duration, date arithmetic]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0002]
source_ids: [SRC-000042, SRC-000013]
acceptance_criteria:
  - Elkülöníti a calendar és elapsed-time arithmeticet.
  - Explicit timezone és boundary policyt követel.
  - SQLite-labelled day-difference példát ad.
---
# Advanced Date and Time Arithmetic

Temporal arithmeticnél különbség van calendar period és elapsed duration között. „Egy hónap” nem
fix másodpercszám; local „egy nap” daylight-saving transitionnél nem mindig 24 elapsed óra.

Rögzítsd, hogy az input instant, local date-time vagy date; milyen timezone és ambiguous/nonexistent
local-time policy érvényes; a boundary inclusive vagy exclusive-e. Storage és presentation timezone
szétválasztása csökkenti a hibát.

Month-end addition, leap day, DST, negative interval és precision loss kötelező edge case. Function
nevek és interval syntax vendorfüggők. String formatting nem temporal arithmetic.

A `SQL-ASQL-0020` SQLite `julianday` alapján két ISO date elapsed napkülönbségét ellenőrzi. Ez nem
PostgreSQL interval execution evidence.

## Források

- [PostgreSQL 18 — Date/Time Functions and Operators](https://www.postgresql.org/docs/18/functions-datetime.html)
- [PostgreSQL 18 — Date/Time Types](https://www.postgresql.org/docs/18/datatype-datetime.html)
