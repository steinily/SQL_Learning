---
schema_version: 1
id: DBKB-ASQL-0011
title: Moving Aggregates
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
prerequisites: [DBKB-ASQL-0009]
related: [DBKB-ASQL-0010, DBKB-ASQL-0021]
aliases: [rolling average]
search_keywords: [moving average, rolling window, preceding rows]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039]
acceptance_criteria:
  - Megkülönbözteti a row-count és time-range ablakot.
  - Tárgyalja a partial frame és missing period hatását.
  - Futtatható háromsoros moving average példát ad.
---
# Moving Aggregates

Moving aggregate bounded frame-en számol, például az aktuális és két előző row átlagán.

```sql
AVG(amount) OVER (
  PARTITION BY account_id
  ORDER BY event_day
  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
) AS moving_average
```

Ez három **row**, nem három calendar nap. Hiányzó napok esetén date scaffold vagy time-range frame kell,
utóbbi syntaxa és boundary behavior-ja engine-specific. Partition első két során partial frame működik;
ha full-window-only metric kell, window counttal guardold.

Duplicate time key peer/tie kérdés és deterministic ordering nélkül row frame bizonytalan lehet.
`NULL` input aggregate semanticsét és denominatorát explicit teszteld.

A `SQL-ASQL-0011` négy egymást követő amounton exact, roundolt három-row moving average-et ellenőriz
SQLite-on.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
