---
schema_version: 1
id: DBKB-ASQL-0004
title: ROW_NUMBER
type: concept
primary_domain: advanced-sql
secondary_domains: [analytics, data-quality]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ASQL-0003]
related: [DBKB-ASQL-0005, DBKB-ASQL-0012]
aliases: [row sequence]
search_keywords: [row_number, ranking, top n, deduplication]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039]
acceptance_criteria:
  - Definiálja a partitionön belüli 1-alapú sequence-et.
  - Deterministic total orderinget követel.
  - Futtatható tie-breaker példát ad.
---
# ROW_NUMBER

`ROW_NUMBER()` minden partition sorait 1-től sorszámozza a window ordering szerint. Peers között is
külön számot ad, ezért a business orderinget unique tie-breakerrel kell teljessé tenni.

```sql
ROW_NUMBER() OVER (
  PARTITION BY customer_id
  ORDER BY event_time DESC, event_id DESC
) AS rn
```

Top-one-per-group és deterministic survivor kiválasztás gyakori használat. A `WHERE rn = 1` filterhez
külső query/CTE szükséges. A survivor rule-t üzletileg dokumentáld; „bármelyik sor” nem auditálható.

`ROW_NUMBER` nem persistent identity és nem változatlan új adatok mellett. Paginationre csak stable
snapshot és teljes order mellett használható.

A `SQL-ASQL-0004` tied timestamp mellett `event_id` tie-breakerrel választ legújabb sort SQLite-on.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
