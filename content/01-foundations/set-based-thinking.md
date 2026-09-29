---
schema_version: 1
id: DBKB-FND-0020
title: Set-Based Thinking
type: concept
primary_domain: foundations
secondary_domains: [sql, performance]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: [portable-sql]
scope: general
prerequisites: [DBKB-FND-0018, DBKB-FND-0019]
related: [DBKB-FND-0017, DBKB-FND-0021, DBKB-FND-0035]
aliases: [set-oriented SQL, declarative thinking]
search_keywords: [row-by-row, RBAR, predicate, bulk operation]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0003]
source_ids: [SRC-000002, SRC-000022]
acceptance_criteria:
  - Elmagyarázza a result-set és predicate alapú megközelítést.
  - Nem állítja, hogy minden row-by-row megoldás hibás vagy lassabb.
  - Bemutatja a correctness és performance ellenőrzési pontokat.
---
# Set-Based Thinking

A **set-based thinking** a kívánt row-halmazt és transformationt írja le, nem egy kézzel vezérelt
row-by-row iterationt. SQL-ben ez lehetővé teszi, hogy az optimizer access patht, join ordert és
parallel executiont válasszon.

## Kérdés újrafogalmazása

Procedural: „Minden ordert beolvasok, megkeresem a customerét, majd frissítem.”

Set-based: „Frissítsd az összes overdue ordert, amelyhez aktív customer tartozik.”

```sql
UPDATE sales_order
SET status = 'OVERDUE'
WHERE due_date < :today
  AND status = 'OPEN';
```

## Előny és kockázat

Egy set statement kevesebb client/server round tripet és nagyobb optimizer freedomot adhat.
Ez nem univerzális performance bizonyíték: execution plan, index, cardinality, logging és lock
scope dönt. Nagy bulk update hosszú transactiont, blockingot és log növekedést okozhat; batch
megoldás indokolt lehet.

## Correctness

Set operation előtt rögzítsd:

- mi a row identity és várható affected cardinality;
- hogyan kezelendő a duplicate és `NULL`;
- determinisztikus-e a tie-breaking;
- transactionben kell-e együtt commitolnia;
- hogyan validálható az előtte/utána state.

## Mikor kell iteration?

External side effect, stateful protocol vagy szigorúan sequential dependency indokolhat
iterationt. Ilyenkor is különítsd el a database set queryt a side-effect loop-tól, használj
idempotencyt és checkpointot. A cél nem dogma, hanem a problem megfelelő absztrakciója.

## Források

- [IBM Research — Relational model](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks)
- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
