---
schema_version: 1
id: DBKB-FND-0022
title: Selectivity
type: concept
primary_domain: foundations
secondary_domains: [performance, sql]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql]
scope: cross-vendor
prerequisites: [DBKB-FND-0021]
related: [DBKB-FND-0008, DBKB-FND-0031]
aliases: [predicate selectivity, filter ratio]
search_keywords: [cardinality estimate, histogram, statistics, distinct]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0004]
source_ids: [SRC-000015]
acceptance_criteria:
  - Képlettel definiálja a predicate selectivityt.
  - Jelzi a high/low terminológia kétértelműségét.
  - Actual példát ad Atlas tiny adaton.
---
# Selectivity

A predicate **selectivity** a megtartott row-k aránya az input cardinalityhez képest:

```text
selectivity = matching_rows / input_rows
```

Három input rowból egy match selectivityje `1/3`. Az estimated output cardinality gyakori
közelítése `input cardinality × estimated selectivity`.

## Terminológiai óvatosság

A „high selectivity” kifejezést egyesek sok distinct value-ra, mások sok kiválasztott row-ra
használják. Félreértés helyett közöld a ratio-t, matching row countot és distinct countot.

## Statistics

Az optimizer histogram, most-common-value frequency, null fraction és distinct estimate alapján
becsülhet. Correlated predicate-ek függetlennek feltételezése súlyos hibát okozhat. PostgreSQL
18 official példái konkrétan bemutatják histogram és MCV használatát; algoritmus és default
version-sensitive.

## Index kapcsolat

Alacsony matching ratio kedvezhet index accessnek, de nem garantálja. Row width, clustering,
cache, covering, random I/O, ordering és fetch cost mind számít. „Selective predicate → index”
csak hypothesis, execution plannel és méréssel ellenőrizendő.

A `SQL-FND-0011` Atlas tiny fixture-ben actual countot és total countot kér le, így a `1/3`
arány tényleges expected resultként validált.

## Forrás

- [PostgreSQL 18 — Row Estimation Examples](https://www.postgresql.org/docs/18/row-estimation-examples.html)
