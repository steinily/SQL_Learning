---
schema_version: 1
id: DBKB-SQL-0019
title: CROSS JOIN
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
scope: portable-sql
prerequisites: [DBKB-SQL-0016]
related: [DBKB-SQL-0017, DBKB-SQL-0004]
aliases: [Cartesian product]
search_keywords: [cross join, Cartesian product, combinations, row explosion]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000029]
acceptance_criteria:
  - Meghatározza a Cartesian product cardinalityjét.
  - Megkülönbözteti a szándékos kombinációt a hiányzó predicate hibától.
  - Futtatható cross join példát ad.
---
# CROSS JOIN

A `CROSS JOIN` mindkét input minden sorpárját előállítja. Ha az input cardinality `m` és `n`, az
eredmény cardinality `m × n`. Nincs `ON` predicate.

```sql
SELECT s.size_code, c.color_code
FROM size_option AS s
CROSS JOIN color_option AS c;
```

Szándékos use case lehet dimension combination, calendar scaffold vagy kis parameter grid. Ugyanez
nagy inputokon row explosiont, memória- és runtime-növekedést okozhat. Az input countok szorzatát
futtatás előtt becsüld, és explicit business reason nélkül ne engedj cross joint production querybe.

Comma-separated `FROM a, b` logical eredménye predicate nélkül szintén Cartesian product lehet, de
az explicit `CROSS JOIN` jobban dokumentálja az intentet. Ha kapcsolatot akartál, hiányzik a join
condition; utólagos `DISTINCT` nem javítja a téves kombinációkat.

## Validation

Ne csak néhány sample sort nézz: ellenőrizd a teljes expected countot, a combination uniquenesset és
az input boundaryket, beleértve az empty inputot. Filter placement jelentősen csökkentheti vagy
megváltoztathatja a productot.

A `SQL-SQL-0019` két size és három color hat exact kombinációját ellenőrzi SQLite-on.

## Források

- [Microsoft — FROM clause plus JOIN](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver17)
