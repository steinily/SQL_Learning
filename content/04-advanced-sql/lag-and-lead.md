---
schema_version: 1
id: DBKB-ASQL-0007
title: LAG and LEAD
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
related: [DBKB-ASQL-0013, DBKB-ASQL-0020]
aliases: [navigation functions]
search_keywords: [lag, lead, previous row, next row, delta]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039]
acceptance_criteria:
  - Meghatározza az offset és default behavior-t.
  - Deterministic orderinget és partition boundaryt követel.
  - Futtatható delta példát ad.
---
# LAG and LEAD

`LAG` korábbi, `LEAD` későbbi sor expression értékét adja ugyanabban a partitionben. Optional offset
és default szabályozza, hány sorral és boundaryn mit kapunk.

```sql
amount - LAG(amount) OVER (
  PARTITION BY account_id ORDER BY event_time, event_id
) AS delta
```

Az „előző” csak teljes orderinggel értelmezhető. Hiányzó calendar napot nem pótol: az előző meglévő
row-t adja, ezért period-over-period elemzéshez calendar scaffold kellhet. PostgreSQL 18-ban a
dokumentált behavior `RESPECT NULLS`; más null-treatment option nem feltételezhető.

Partition első/utolsó során default nélkül `NULL` lesz. Ne `COALESCE`-old automatikusan zeróra, ha a
missing predecessor üzletileg más állapot.

A `SQL-ASQL-0007` két account timeline-ján previous amountot és delta-t ellenőriz SQLite-on.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
