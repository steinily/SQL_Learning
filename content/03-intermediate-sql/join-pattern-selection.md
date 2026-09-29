---
schema_version: 1
id: DBKB-ISQL-0005
title: Join Pattern Selection
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
scope: cross-vendor
prerequisites: [DBKB-SQL-0016, DBKB-SQL-0018]
related: [DBKB-ISQL-0007, DBKB-ISQL-0008]
aliases: [logical join selection]
search_keywords: [inner join, outer join, semi join, anti join, cardinality]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0001]
source_ids: [SRC-000029, SRC-000033, SRC-000036]
acceptance_criteria:
  - Business questionből vezeti le a logical join formát.
  - Megköveteli az output grain és cardinality rögzítését.
  - Futtatható összehasonlító példát ad.
---
# Join Pattern Selection

Logical join mintát az elvárt output határoz meg, nem a várható physical algorithm.

| Kérdés | Minta | Cardinality-hatás |
|---|---|---|
| Csak matching párok | `INNER JOIN` | minden match combination |
| Bal sorok match nélkül is | `LEFT JOIN` | legalább a bal oldal |
| Van-e legalább egy match | `EXISTS` | legfeljebb egy output bal soronként |
| Nincs-e match | `NOT EXISTS` | csak unmatched bal sorok |
| Minden kombináció kell | `CROSS JOIN` | bal × jobb |

Ha jobb oldali attributum kell, semi join nem elegendő. Ha csak existence kell, inner join plusz
`DISTINCT` elfedheti a jobb oldali multiplicityt. Outer joinnál az `ON` és `WHERE` filter placement
megváltoztathatja az unmatched sorok megőrzését.

Review előtt rögzítsd mindkét input grain-jét, key uniquenessét/nullabilityjét, az expected row count
tartományt és a duplicate policyt. Az optimizer később több logical formát azonos physical planre
írhat át, de erre correctnesset nem építünk.

A `SQL-ISQL-0005` ugyanazon fixture-en inner join countot és existence-preserved countot ad vissza,
megmutatva a multiplicity különbséget.

## Források

- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
