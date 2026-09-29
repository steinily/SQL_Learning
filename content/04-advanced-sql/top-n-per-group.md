---
schema_version: 1
id: DBKB-ASQL-0012
title: Top N per Group
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
prerequisites: [DBKB-ASQL-0004, DBKB-ASQL-0005]
related: [DBKB-ISQL-0023]
aliases: [greatest n per group]
search_keywords: [top n, row_number, rank, per group]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039, SRC-000040]
acceptance_criteria:
  - Megkülönbözteti a pontos N sort és tie-inclusive eredményt.
  - Deterministic survivor orderinget követel.
  - Futtatható top-two példát ad.
---
# Top N per Group

Top-N-per-group query előbb partitionön belül rankol, majd külső queryben szűr. Pontosan legfeljebb
`N` sorhoz `ROW_NUMBER`; a boundary tie-ok megtartásához a business szabály szerint `RANK` vagy
`DENSE_RANK` használható.

```sql
WITH ranked AS (
  SELECT o.*,
         ROW_NUMBER() OVER (
           PARTITION BY customer_id
           ORDER BY amount DESC, order_id
         ) AS rn
  FROM sales_order AS o
)
SELECT * FROM ranked WHERE rn <= 2;
```

Unique tie-breaker nélkül a kiválasztott sorok változhatnak. A window outputra ugyanazon query block
`WHERE` clause-ában nem szűrünk; CTE vagy derived table ad boundaryt. Index/performance kérdéshez plan
és data distribution kell.

A `SQL-ASQL-0012` két customeren exact top-two ordert ellenőriz SQLite-on.

## Források

- [PostgreSQL 18 Tutorial — Window Functions](https://www.postgresql.org/docs/18/tutorial-window.html)
