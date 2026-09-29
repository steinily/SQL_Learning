---
schema_version: 1
id: DBKB-ASQL-0009
title: Window Frames
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
prerequisites: [DBKB-ASQL-0003]
related: [DBKB-ASQL-0008, DBKB-ASQL-0010, DBKB-ASQL-0011]
aliases: [rows range groups frame]
search_keywords: [window frame, rows, range, groups, unbounded preceding]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039, SRC-000040]
acceptance_criteria:
  - Elkülöníti a partitiont a frame-től.
  - Bemutatja a ROWS és peer-sensitive default különbségét.
  - Futtatható tie-frame ellenpéldát ad.
---
# Window Frames

Partition a window teljes logical csoportja; frame az aktuális sorhoz tartozó részhalmaz, amelyen a
frame-sensitive function számol. `ROWS`, `RANGE` és `GROUPS` eltérő unitot használhat, támogatásuk és
részletes syntaxuk verziófüggő.

Ordered window default frame-je peer-sensitive. Running totalhoz az explicit
`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` row-by-row viselkedést ad; `RANGE` peers mellett
egyszerre több sort foghat be.

Moving window például `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`. Partition boundaryn a frame kisebb
lesz, nem képződik automatikus missing row. Date-range frame semanticse type- és engine-specific.

A `SQL-ASQL-0009` tied order key mellett összeveti a default peer-sensitive és explicit `ROWS`
running sumot SQLite-on.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
- [PostgreSQL 18 Tutorial — Window Functions](https://www.postgresql.org/docs/18/tutorial-window.html)
