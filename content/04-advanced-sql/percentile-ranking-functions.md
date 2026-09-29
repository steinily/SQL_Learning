---
schema_version: 1
id: DBKB-ASQL-0006
title: Percentile Ranking Functions
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
prerequisites: [DBKB-ASQL-0005]
related: [DBKB-ASQL-0009]
aliases: [percent_rank, cume_dist, ntile]
search_keywords: [percent_rank, cume_dist, ntile, percentile]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039]
acceptance_criteria:
  - Megkülönbözteti a percent_rank cume_dist és ntile jelentését.
  - Tárgyalja a peer és small-partition edge case-eket.
  - Futtatható cume distribution példát ad.
---
# Percentile Ranking Functions

`PERCENT_RANK` a rank relatív helyét, `CUME_DIST` az aktuális peer groupig bezárólag a partition
arányát, `NTILE(n)` pedig közel egyenlő sorszámú bucketet ad. Ezek nem cserélhetők fel statistical
percentile calculationnel.

Peers azonos `PERCENT_RANK` és `CUME_DIST` értéket kapnak. Small partition, single row és `n`-nél
kevesebb row esetén boundary behavior-t teszttel rögzítsd. Floating-point eredményt tolerance-szal
vagy stabil text/round contracttal hasonlíts production testben.

`NTILE` row-count bucketeket képez, nem equal value-range-et; skewed distributionnél a business
interpretáció félrevezető lehet. Final presentation order külön clause.

A `SQL-ASQL-0006` négy score-on `CUME_DIST` értéket ellenőriz SQLite-on, roundolt outputtal.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
