---
schema_version: 1
id: DBKB-ASQL-0021
title: Temporal Bucketing
type: concept
primary_domain: advanced-sql
secondary_domains: [analytics, temporal-data]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ASQL-0020, DBKB-ISQL-0004]
related: [DBKB-ASQL-0011]
aliases: [time bucket, date truncation]
search_keywords: [date_trunc, time bucket, calendar, timezone]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0002]
source_ids: [SRC-000042]
acceptance_criteria:
  - Bucket origin width és timezone contractot követel.
  - Elkülöníti a truncationt a complete-series generálástól.
  - SQLite-labelled month-bucket példát ad.
---
# Temporal Bucketing

Time bucket timestampet intervalhoz vagy calendar periodhoz rendel. Contractja a bucket width,
origin, timezone és half-open boundary `[start,end)`. Ezek nélkül ugyanaz az event más bucketbe kerülhet.

PostgreSQL `date_trunc` calendar fieldre csonkol; más engine functionje és week originje eltérhet.
Truncation csak meglévő eventeket csoportosít, missing bucketet nem generál. Complete time serieshez
calendar/date spine és outer join kell.

Local-time bucket DST-nél eltérő elapsed hosszúságú lehet. Analyticsnél döntsd el, business local
calendar vagy UTC elapsed interval a kívánt fogalom. Index usage és expression index támogatás
engine-specific.

A `SQL-ASQL-0021` ISO timestamp prefixből SQLite-on havi countot képez explicit ordered outputtal.

## Források

- [PostgreSQL 18 — Date/Time Functions and Operators](https://www.postgresql.org/docs/18/functions-datetime.html)
