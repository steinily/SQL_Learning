---
schema_version: 1
id: DBKB-ISQL-0006
title: Self Joins
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
prerequisites: [DBKB-SQL-0017, DBKB-FND-0019]
related: [DBKB-ISQL-0022, DBKB-SQL-0018]
aliases: [recursive relationship join]
search_keywords: [self join, hierarchy, parent, manager, adjacency list]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0001]
source_ids: [SRC-000036]
acceptance_criteria:
  - Aliasokkal külön szerepként kezeli ugyanazt a table-t.
  - Bemutatja a parent-child outer join használatot.
  - Futtatható employee-manager példát ad.
---
# Self Joins

Self join ugyanazt a table-t két vagy több logical szerepben használja. Minden szerepnek külön alias
kell; így egy adjacency-list hierarchyban az egyik alias child, a másik parent.

```sql
SELECT e.employee_name, m.employee_name AS manager_name
FROM employee AS e
LEFT JOIN employee AS m
  ON m.employee_id = e.manager_id;
```

A `LEFT JOIN` megtartja a root alkalmazottat, akinek `manager_id` értéke `NULL`. `INNER JOIN` ezt a
sort eldobná. Egyetlen self join csak egy relationship lépést jár be; tetszőleges mélységhez recursive
CTE vagy más hierarchy feature szükséges.

Peer-párok képzésénél könnyű symmetric duplicate-ot létrehozni: `a.id < b.id` egy irányra korlátozza
a párokat, míg `a.id <> b.id` mindkét irányt visszaadja. Cycle és orphan ellenőrzés az adatmodell
felelőssége; foreign key önmagában cycle-t engedhet.

A `SQL-ISQL-0006` rootot és két childot tartalmaz, és exact employee–manager outputot validál
SQLite-on.

## Források

- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
