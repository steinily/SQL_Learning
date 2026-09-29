---
schema_version: 1
id: DBKB-ASQL-0002
title: Window Function Fundamentals
type: concept
primary_domain: advanced-sql
secondary_domains: [analytics]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0013, DBKB-ISQL-0002]
related: [DBKB-ASQL-0003, DBKB-ASQL-0009]
aliases: [analytic function]
search_keywords: [window, over, partition by, analytic]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039, SRC-000040]
acceptance_criteria:
  - Elkülöníti a window és grouped aggregate row behavior-ját.
  - Bemutatja az OVER clause szerepét.
  - Futtatható partition aggregate példát ad.
---
# Window Function Fundamentals

Window function kapcsolódó sorok fölött számol úgy, hogy az input sorok identitása megmarad. Ugyanaz
az `AVG` `OVER` nélkül group aggregate, `OVER` clause-zal window aggregate.

```sql
SELECT employee_id, department_id, salary,
       AVG(salary) OVER (PARTITION BY department_id) AS department_average
FROM employee;
```

Az `OVER` három külön semantic dimenziót tartalmazhat: `PARTITION BY` létrehozza a független
ablakrészeket, `ORDER BY` sorrendet és peer groupokat definiál, a frame pedig az aktuális sorhoz
látható részhalmazt. Nem minden window function használja mindhármat azonos módon.

Window function a PostgreSQL logical processing szerint select listben és final `ORDER BY`-ban
használható; eredményére szűréshez query boundary szükséges. Az optimizer physical megvalósítását
nem a syntaxból vezetjük le.

A `SQL-ASQL-0002` department average-et számol, miközben minden employee sor megmarad SQLite-on.

## Források

- [PostgreSQL 18 Tutorial — Window Functions](https://www.postgresql.org/docs/18/tutorial-window.html)
- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
