---
schema_version: 1
id: DBKB-FND-0006
title: Relational Model Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [data-modeling, sql]
levels: [beginner, intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: [portable-sql, sqlite]
scope: general
prerequisites: [DBKB-FND-0002, DBKB-FND-0003]
related: [DBKB-FND-0007, DBKB-FND-0008, DBKB-FND-0009, DBKB-FND-0019, DBKB-FND-0020]
aliases: [relational model, relation, tuple, attribute]
search_keywords: [reláció, tuple, attribute, domain, key, data independence]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0001]
source_ids: [SRC-000002, SRC-000003]
acceptance_criteria:
  - Bemutatja a relation, tuple, attribute, domain és key fogalmát.
  - Elkülöníti a formal relational modelt az SQL table megvalósítástól.
  - Kapcsolja a modellt a data independence és set-based műveletek céljához.
---
# Relational Model Fundamentals

A **relational model** az adatot relationök formájában írja le, és formális alapot ad a
relationök lekérdezéséhez és átalakításához. E. F. Codd 1970-es elsődleges tanulmánya n-ary
relationökre épülő modellt vezetett be, miközben azt a célt hangsúlyozta, hogy a felhasználó és
az alkalmazás ne függjön a belső gépi reprezentáció változásaitól.

## A relation elemei

Egy relation fogalmi összetevői:

- **Attribute:** named tulajdonság, például `customer_id` vagy `country_code`.
- **Domain:** az attribute megengedett értékkészlete és jelentése. A SQL data type ennek
  fontos, de nem mindig teljes megvalósítása; a business szabály gyakran további constraintet
  igényel.
- **Tuple:** egy állítás a relationben, attribute–value párok együttese.
- **Relation:** azonos headinggel rendelkező tuple-ök halmaza.
- **Heading:** az attribute-ok és domainjeik szerkezete.
- **Body:** az adott időpontban a relationhöz tartozó tuple-ök halmaza.

A „halmaz” szó következménye, hogy a formal relationben nincs duplicate tuple és nincs
lényegi tuple-order. A megjelenítési sorrend nem része a relation jelentésének.

## Key és identity

A **candidate key** olyan minimális attribute-készlet, amely egy tuple-t egyedileg azonosít.
Több candidate key közül a tervező kijelölhet egyet **primary key** szerepre; a többi
alternate key marad. A **foreign key** egy másik relation azonosítható tuple-jére utal, és a
referential integrity gyakorlati eszköze.

A key nem pusztán performance feature. Elsődleges szerepe az identity és integritás. Az index
gyakran segíti a key enforcementet vagy lookupot, de a constraint és az index fogalma nem
azonos.

## Relational műveletek

A relationből új relation képezhető. Alapvető műveleti ötletek:

- **selection:** tuple-ök kiválasztása predicate alapján;
- **projection:** attribute-ok kiválasztása;
- **join:** összetartozó tuple-ök kombinálása közös feltétel alapján;
- **union, intersection, difference:** kompatibilis relationök set műveletei;
- **rename:** attribute vagy relation logikai átnevezése.

Az eredmény closure elve szerint ismét relation, ezért a műveletek kompozícióba rendezhetők.
Ez támogatja a **declarative** gondolkodást: elsősorban a kívánt eredményt írjuk le, nem a
page-ek bejárásának algoritmusát.

## Formal relation és SQL table

Az SQL relational alapú, de gyakorlati nyelve és product implementációi nem azonosak a tiszta
matematikai modellel:

- SQL query explicit `DISTINCT` nélkül duplicate row-kat is adhat.
- SQL támogatja a `NULL` markert és a [three-valued logic](null-fundamentals.md) következményeit.
- A table rendelkezhet fizikai storage, index és partition tulajdonságokkal.
- A row order `ORDER BY` nélkül nincs garantálva; ezt a PostgreSQL 18 Concepts oldal is
  explicit rögzíti.

Ezért hasznos a pontos nyelv: formal állításnál relation/tuple/attribute, SQL implementation
esetén table/row/column. Oktatási helyzetben megfeleltethetők, de a különbségeket nem szabad
eltüntetni.

## Mini példa

Az Atlas `customer` table-ből a magyar customerök kódját és nevét kérjük. A predicate a
selection, a két kiválasztott column a projection SQL-megfelelője:

```sql
SELECT customer_code, customer_name
FROM customer
WHERE country_code = 'HU'
ORDER BY customer_code;
```

Az `ORDER BY` nem a relation fogalmi része; a determinisztikus megjelenítéshez adjuk hozzá. A
példa tényleges execution evidence-ét a `SQL-FND-0001` rekord tárolja.

## Data independence

A relational megközelítés lényegi mérnöki értéke, hogy a logical kérdés elválasztható a
physical access pathtól. Ugyanarra a queryre az optimizer választhat scan, index lookup vagy
join algorithm közül anélkül, hogy a consumer új üzleti kérdést fogalmazna. Ez nem jelent
korlátlan függetlenséget: schema change, type change vagy eltérő transaction semantics
megváltoztathatja a látható contractot.

## Gyakori tévedések

- A relation nem a row-k tárolási sorrendje.
- A foreign key nem ugyanaz, mint egy application-side object reference.
- A relational model nem azt állítja, hogy minden adatot egyetlen table-be kell tenni.
- Az SQL syntax ismerete nem helyettesíti a key, integrity és logical modeling megértését.

## Források

- [IBM Research — A Relational Model of Data for Large Shared Data Banks](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks) — Codd eredeti tanulmánya és abstractja.
- [PostgreSQL 18 — SQL Concepts](https://www.postgresql.org/docs/18/tutorial-concepts.html) — a relation/table, named rows/columns/types és rendezetlen row eredmény official leírása.
