---
schema_version: 1
id: DBKB-ISQL-0022
title: Recursive CTE Fundamentals and Safety
type: concept
primary_domain: intermediate-sql
secondary_domains: [data-modeling, operations]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0020, DBKB-ISQL-0015]
related: [DBKB-ISQL-0006]
aliases: [with recursive, hierarchy traversal]
search_keywords: [recursive cte, anchor, recursive term, cycle, termination]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ISQL-0003]
source_ids: [SRC-000032]
acceptance_criteria:
  - Elkülöníti az anchor és recursive termet.
  - Kötelező termination és cycle guardot ad.
  - Futtatható bounded recursive példát ad.
---
# Recursive CTE Fundamentals and Safety

Recursive CTE saját outputjára hivatkozhat. Szerkezete anchor termből és recursive termből áll,
amelyeket tipikusan `UNION ALL` kapcsol össze. Hierarchy, graph reachability és sequence generálás
gyakori use case.

```sql
WITH RECURSIVE numbers(n) AS (
  VALUES (1)
  UNION ALL
  SELECT n + 1 FROM numbers WHERE n < 5
)
SELECT n FROM numbers;
```

A termination guard correctness és resource safety feltétel. Graphon explicit visited-path vagy
engine-supported cycle detection kellhet; egyszerű depth limit csak safety brake, nem cycle
correctness bizonyíték. `UNION` duplicate elimination néha megállít ismétlést, de eltérő path/depth
columnok mellett nem általános megoldás.

Traversal order nem implicit result order. Ha breadth/depth presentation kell, számíts ordering key-t
és a végén rendezz. Recursion limit és syntax vendor/version-sensitive.

A `SQL-ISQL-0022` explicit `n < 5` guarddal pontosan 1–5 sorokat generál SQLite-on.

## Források

- [PostgreSQL 18 — WITH Queries](https://www.postgresql.org/docs/18/queries-with.html)
