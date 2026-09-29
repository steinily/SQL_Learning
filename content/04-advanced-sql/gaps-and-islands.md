---
schema_version: 1
id: DBKB-ASQL-0013
title: Gaps and Islands
type: recipe
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
prerequisites: [DBKB-ASQL-0007, DBKB-ASQL-0004]
related: [DBKB-ASQL-0020, DBKB-ASQL-0021]
aliases: [consecutive ranges]
search_keywords: [gaps, islands, consecutive, lag, sequence]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039]
acceptance_criteria:
  - A consecutiveness business definíciójából indul ki.
  - LAG és cumulative group mintát mutat.
  - Futtatható integer-island példát ad.
---
# Gaps and Islands

Gaps-and-islands pattern consecutive értékek összefüggő szakaszait keresi. Előbb pontosan definiáld,
mi a „következő”: integer +1, következő calendar nap, vagy tolerancián belüli timestamp.

Egy általános lépés: `LAG`-gel jelöld az új island kezdetét, majd a flag cumulative sumja legyen a
group id. Ezután grouponként `MIN`, `MAX` és `COUNT` adja a tartományt.

Duplicate timestamp/key, missing calendar day és timezone/DST megváltoztathatja az eredményt. Input
deduplication csak explicit grain alapján történjen. Sequence arithmetic type overflow-t és calendar
semantics-et is figyelembe kell venni.

A `SQL-ASQL-0013` integer sorozaton `1–3`, `5–6`, `9` islandeket képez és exact boundaryket validál
SQLite-on.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
