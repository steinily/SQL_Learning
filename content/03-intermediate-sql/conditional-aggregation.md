---
schema_version: 1
id: DBKB-ISQL-0003
title: Conditional Aggregation
type: concept
primary_domain: intermediate-sql
secondary_domains: [analytics]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: portable-sql
prerequisites: [DBKB-SQL-0013, DBKB-SQL-0010]
related: [DBKB-ISQL-0018, DBKB-ISQL-0019]
aliases: [case aggregation]
search_keywords: [sum case, conditional count, pivot-like aggregation]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0001, RP-ISQL-0003]
source_ids: [SRC-000027, SRC-000035]
acceptance_criteria:
  - Bemutatja a CASE-in-aggregate mintát.
  - Tisztázza az ELSE és NULL következményét.
  - Futtatható conditional count példát ad.
---
# Conditional Aggregation

Conditional aggregation ugyanazon groupból több feltételes measure-t állít elő. Portable minta a
`CASE` expression aggregate-be helyezése.

```sql
SELECT customer_id,
       SUM(CASE WHEN status = 'OPEN' THEN 1 ELSE 0 END) AS open_count,
       SUM(CASE WHEN status = 'CLOSED' THEN 1 ELSE 0 END) AS closed_count
FROM sales_order
GROUP BY customer_id;
```

Az `ELSE 0` biztosítja, hogy nem matching sor is numerikus nullával járuljon hozzá. `ELSE` nélkül a
`CASE` `NULL`-t ad; a `SUM` ezt ignorálja, és olyan groupban, ahol nincs match, az eredmény `NULL`
lehet. `COUNT(CASE WHEN ... THEN 1 END)` más, de gyakran szándékos forma.

Overlapping conditionök ugyanazt a sort több bucketbe számolhatják. Ha a bucketeknek kölcsönösen
kizárónak és teljesnek kell lenniük, ezt külön data-quality assertionnel ellenőrizd. Nullable status
számára is legyen explicit branch vagy dokumentált exclusion.

PostgreSQL aggregate `FILTER` clause kényelmes alternatíva, de a portable példa `CASE`-t használ.
A `SQL-ISQL-0003` két customer open/closed countját exact sorokkal validálja.

## Források

- [PostgreSQL 18 — Aggregate Functions](https://www.postgresql.org/docs/18/functions-aggregate.html)
- [PostgreSQL 18 — Conditional Expressions](https://www.postgresql.org/docs/18/functions-conditional.html)
