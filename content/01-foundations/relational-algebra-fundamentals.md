---
schema_version: 1
id: DBKB-FND-0019
title: Relational Algebra Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [sql, data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: [portable-sql, sqlite]
scope: general
prerequisites: [DBKB-FND-0006, DBKB-FND-0018]
related: [DBKB-FND-0020, DBKB-FND-0035]
aliases: [selection, projection, join, relational operations]
search_keywords: [sigma, pi, union, difference, Cartesian product, closure]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0003]
source_ids: [SRC-000002, SRC-000022]
acceptance_criteria:
  - Bemutatja a selection, projection, rename, product, join és set operation szerepét.
  - Kiemeli a closure és composition jelentőségét.
  - SQL példát ad a megfeleltetésre anélkül, hogy azonosságot állítana.
---
# Relational Algebra Fundamentals

A **relational algebra** relationöket vesz inputként és relationt ad outputként. A closure
miatt a műveletek egymásba ágyazhatók, ami a declarative query composability formális alapja.

## Alapműveletek

- **Selection (`σ`):** tuple-öket szűr predicate alapján; SQL-ben tipikusan `WHERE`.
- **Projection (`π`):** attribute-okat választ; SQL `SELECT` listához hasonló, de SQL duplicate
  behavior miatt nem teljes azonosság.
- **Rename (`ρ`):** relation vagy attribute nevét változtatja a composition érdekében.
- **Cartesian product (`×`):** minden tuple-kombinációt képez.
- **Union/difference:** union-compatible relationök set műveletei.
- **Join:** product és predicate kombinációjaként összetartozó tuple-öket kapcsol.

## Példa

```sql
SELECT c.customer_code, o.sales_order_id
FROM customer AS c
JOIN sales_order AS o
  ON o.customer_id = c.customer_id
WHERE o.status = 'NEW'
ORDER BY o.sales_order_id;
```

A join combinationt képez, a `WHERE` selectiont végez, a select list projection jellegű. Az
`ORDER BY` presentation operation; nem része a formal relationnek. A `SQL-FND-0009` ezt a
declared portable subsetet Atlas-szerű fixture-rel futtatja.

## Equivalence és optimizer

Algebrai equivalence-ek lehetővé teszik a query rewrite-ot: selection pushdown vagy join order
változtatás csökkentheti az intermediate resultot. Null semantics, duplicate bag behavior,
outer join és volatile function azonban korlátozhatja az egyszerű átalakítást. A formal set
equivalence-t nem szabad automatikusan SQL query equivalence-nek venni.

## Miért hasznos?

Segít a queryt logical lépésekre bontani, felismerni a fölösleges productot/duplicate-ot és
érteni, miért választhat több physical execution plant ugyanarra a result contractra.

## Források

- [IBM Research — Codd 1970](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks)
- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
