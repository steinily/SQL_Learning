---
schema_version: 1
id: DBKB-ISQL-0013
title: EXISTS
type: concept
primary_domain: intermediate-sql
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: portable-sql
prerequisites: [DBKB-ISQL-0012]
related: [DBKB-ISQL-0007, DBKB-ISQL-0014]
aliases: [existence predicate]
search_keywords: [exists, correlated subquery, semi join]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000033]
acceptance_criteria:
  - Row existenceként definiálja az EXISTS eredményét.
  - Tisztázza a select list irrelevanciáját és side-effect tiltást.
  - Pozitív és negatív futtatható esetet ad.
---
# EXISTS

Az `EXISTS(subquery)` `TRUE`, ha a subquery legalább egy sort ad, és `FALSE`, ha egyet sem. Nem a
select-list value-ja számít; ezért a `SELECT 1` olvasható convention.

```sql
SELECT c.customer_id
FROM customer AS c
WHERE EXISTS (
  SELECT 1 FROM sales_order AS o
  WHERE o.customer_id = c.customer_id
);
```

PostgreSQL dokumentáció szerint a rendszer általában csak addig értékeli a subqueryt, amíg az
existence eldől; erre támaszkodva se írj side effectet, mert evaluation nem application contract.

Az `EXISTS` természetesen kezeli, ha a matching row valamely output columnja `NULL`, hiszen a row
létezése számít. Ez előnyösebb lehet nullable membership összehasonlításnál. Multiple match nem
sokszorozza a külső sort.

A `SQL-ISQL-0013` egy correlated `EXISTS`-szel pontosan a rendelkező customereket adja vissza.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
