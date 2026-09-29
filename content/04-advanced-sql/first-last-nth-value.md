---
schema_version: 1
id: DBKB-ASQL-0008
title: FIRST_VALUE LAST_VALUE and NTH_VALUE
type: concept
primary_domain: advanced-sql
secondary_domains: [analytics]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ASQL-0003, DBKB-ASQL-0009]
related: [DBKB-ASQL-0007]
aliases: [window value functions]
search_keywords: [first_value, last_value, nth_value, frame]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039]
acceptance_criteria:
  - Frame-relative value-ként magyarázza a három functiont.
  - Bemutatja a default LAST_VALUE csapdát.
  - Explicit full-partition frame példát ad.
---
# FIRST_VALUE LAST_VALUE and NTH_VALUE

Ezek a functionök a **window frame** első, utolsó vagy n-edik sorának value-ját adják, nem automatikusan
a teljes partitionét. Ordered window default frame-je a current peer groupig terjedhet, ezért a
`LAST_VALUE` gyakran az aktuális sort adja a várt partition-end helyett.

```sql
LAST_VALUE(amount) OVER (
  PARTITION BY account_id ORDER BY event_time, event_id
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
)
```

Az explicit full-partition frame teszi láthatóvá az intentet. `NTH_VALUE` insufficient frame esetén
`NULL`; az `n` 1-alapú. PostgreSQL null treatmentje a dokumentált defaultot követi, vendor feature-t
ne generalizálj.

A `SQL-ASQL-0008` first és last amountot minden partition row mellett ellenőriz SQLite-on explicit
frame-mel.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
