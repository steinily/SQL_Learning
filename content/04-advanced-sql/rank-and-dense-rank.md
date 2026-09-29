---
schema_version: 1
id: DBKB-ASQL-0005
title: RANK and DENSE_RANK
type: comparison
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
related: [DBKB-ASQL-0004, DBKB-ASQL-0006]
aliases: [ranking with ties]
search_keywords: [rank, dense_rank, peers, gaps]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039]
acceptance_criteria:
  - Összehasonlítja a tie és gap semantics-et.
  - Megkülönbözteti a ROW_NUMBER eredményétől.
  - Futtatható tied-rank példát ad.
---
# RANK and DENSE_RANK

Mindkét function azonos rankot ad az azonos window order key-jű peer soroknak. `RANK` a következő
értéknél rést hagy; `DENSE_RANK` nem.

Például score-ok `100, 100, 90` esetén `RANK` eredménye `1,1,3`, `DENSE_RANK` eredménye `1,1,2`.
`ROW_NUMBER` ezzel szemben `1,2,3`, de a peers belső sorrendjéhez tie-breaker kell.

„Top 3” ezért két külön business kérdés lehet: pontosan három sor, vagy mindenki az első három distinct
score-ban. Előbbi `ROW_NUMBER`, utóbbi gyakran `DENSE_RANK`; `RANK <= 3` a gaps miatt ismét más lehet.

Final output ordert külön add meg. A `SQL-ASQL-0005` mindhárom rank sequence-et exact tie fixture-rel
ellenőrzi SQLite-on.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
