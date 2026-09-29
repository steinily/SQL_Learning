---
schema_version: 1
id: DBKB-SQL-0018
title: OUTER JOIN
type: concept
primary_domain: sql-fundamentals
secondary_domains: [data-modeling]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0016, DBKB-FND-0017]
related: [DBKB-SQL-0017, DBKB-SQL-0006]
aliases: [left join, right join, full join]
search_keywords: [left outer join, unmatched, null extension, full outer join]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000029]
acceptance_criteria:
  - Bemutatja a preserved oldal és null extension fogalmát.
  - Elmagyarázza az ON és WHERE placement kockázatát.
  - Futtatható LEFT JOIN példát ad.
---
# OUTER JOIN

Outer join a matching sorok mellett legalább az egyik oldal unmatched sorait is megőrzi. `LEFT JOIN`
a bal oldalt, `RIGHT JOIN` a jobb oldalt, `FULL OUTER JOIN` mindkettőt preserve-olja; a hiányzó oldal
columnjai `NULL`-lal egészülnek ki.

```sql
SELECT c.customer_id, o.order_id
FROM customer AS c
LEFT JOIN sales_order AS o
  ON o.customer_id = c.customer_id;
```

Az `ON` részeként adott jobb oldali condition a match-et korlátozza, miközben a bal unmatched sor
megmaradhat. Ugyanez a condition `WHERE`-ben az output null-extended sorát is eldobhatja, így a query
inner-like eredményt ad. Ez az egyik leggyakoribb outer join correctness hiba.

## Counting

Customerenként ordert számolva `COUNT(*)` a preserved customer sort is számolja, míg
`COUNT(o.order_id)` csak nem-`NULL` matched order key-t. A megfelelő expression a business questiontől
függ. Nullable business column nem feltétlen alkalmas match existence jelzőnek; használj non-null key-t.

`RIGHT` és `FULL` támogatás, valamint optimizer rewrite verzió- és engine-specifikus. A
`SQL-SQL-0018` ezért csak portable `LEFT JOIN` semanticset futtat SQLite-on, benne egy order nélküli
customerrel.

## Források

- [Microsoft — FROM clause plus JOIN](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver17)
