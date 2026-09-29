---
schema_version: 1
id: DBKB-FND-0003
title: Database Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [database-engineering, operations]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: []
scope: general
prerequisites: [DBKB-FND-0002]
related: [DBKB-FND-0004, DBKB-FND-0005, DBKB-FND-0023, DBKB-FND-0031]
aliases: [database, DB, datastore]
search_keywords: [adatbázis, DBMS, persistence, query, transaction, catalog]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0001]
source_ids: [SRC-000001, SRC-000002, SRC-000003]
acceptance_criteria:
  - Meghatározza a database és DBMS fogalmát anélkül, hogy relational rendszerre szűkítené.
  - Szétválasztja a logical, physical és operational nézőpontot.
  - Bemutatja a fő database responsibility és trade-off területeket.
---
# Database Fundamentals

A **database** tartósan kezelt információ vagy adat szervezett repository-ja. Nem szükségképpen
relational: lehet document, key-value, graph, time-series vagy más modellel szervezett rendszer.
A NIST glossary definíciója is szándékosan tág, és nem köti a fogalmat hagyományos relational
megvalósításhoz.

A **Database Management System (DBMS)** az a software, amely a database létrehozását,
lekérdezését, módosítását, védelmét és üzemi kezelését biztosítja. A database a kezelt adat és
struktúra; a DBMS a kezelő rendszer. A hétköznapi beszédben a két fogalom gyakran összemosódik,
de architecture és troubleshooting során fontos a különbség.

## Három nézőpont

### Logical model

A logical model azt írja le, milyen entity, attribute, relation vagy más szerkezet látható a
felhasználónak. Ide tartozik a schema, a type és a constraint. A logical model kérdése például:
„Egy order pontosan egy customerhez tartozik-e?”

### Physical representation

A physical representation azt írja le, hogyan kerülnek az adatok page-ekre, file-okba,
partitionökbe, indexekbe vagy logokba. Ennek kérdése például: „Mely access path csökkenti a
szükséges I/O-t?” A logical és physical réteg összefügg, de nem azonos. Egy index hozzáadása
normál esetben nem változtatja meg a lekérdezés üzleti jelentését.

### Operational system

Az operational nézőpont a futó szolgáltatásra figyel: availability, backup, recovery,
security, monitoring, capacity, deployment és incident response. Egy helyes schema önmagában
nem tesz egy database-t biztonságossá vagy helyreállíthatóvá.

## A DBMS fő felelősségei

Egy DBMS képességei modellenként és termékenként eltérnek, de a következő felelősségek
gyakoriak:

- **Definition:** schema, object, type és constraint kezelése.
- **Manipulation:** adatok létrehozása, olvasása, módosítása és törlése.
- **Query processing:** declarative vagy procedural kérés végrehajtása.
- **Integrity:** deklarált szabályok és kapcsolatok védelme.
- **Concurrency:** több session vagy worker összehangolása.
- **Transaction management:** összetartozó műveletek boundary-jának és outcome-jának kezelése.
- **Durability and recovery:** log, checkpoint, backup és restore mechanizmusok.
- **Security:** authentication, authorization, encryption és audit lehetőségek.
- **Metadata:** schema és operational állapot leírása catalogokban.

E lista nem állítja, hogy minden database minden tulajdonságot azonos erősséggel biztosít.
Egy embedded database, egy distributed key-value store és egy enterprise RDBMS eltérő
trade-offokat vállalhat.

## Relational database mint konkrét modell

Egy relational DBMS relationökben kezelt adatot és azokon végzett műveleteket tesz elérhetővé.
A PostgreSQL 18 official tutorial konkrétan relational DBMS-ként írja le a rendszert, a table-t
pedig named row collectionként, amelyben a row-k azonos named column készlettel és typed
columnokkal rendelkeznek. Ugyanez a dokumentáció külön figyelmeztet arra, hogy explicit
sorting nélkül nincs garantált row order.

Az SQL table és a matematikai relation azonban nem tökéletesen azonos. SQL-ben előfordulhat
duplicate row és `NULL`, a product pedig fizikai tárolási és execution részleteket is
hozzáad. A formal alapot a [Relational Model Fundamentals](relational-model-fundamentals.md)
ismerteti.

## Database boundary

Egy rendszertervben mindig nevezd meg, mit tekintesz database boundary-nak. PostgreSQL
terminológiában egy server instance több database-t kezelhet; más vendor ugyanazokat a
szavakat más hierarchy mellett használhatja. A „database” szó ezért nem elég pontos egy
deployment diagramon: add meg az engine-t, a versiont és az object hierarchy szintjét.

Hasonlóan fontos a **system of record** fogalom. Attól, hogy egy dataset database-ben van,
még nem biztos, hogy az az authoritative forrás. Cache, replica, warehouse projection vagy
search index is tárolhat adatot, miközben a canonical ownership máshol marad.

## Trade-off kérdések

Database választáskor ne csak feature listát hasonlíts össze. Vizsgáld meg:

- milyen access pattern és consistency guarantee szükséges;
- mekkora latency, throughput és data volume várható;
- kell-e multi-row transaction vagy cross-region availability;
- hogyan történik backup, restore és schema evolution;
- milyen query, operational és security szakértelem áll rendelkezésre;
- mennyire hordozható a logical model és az alkalmazás.

Egy technology akkor megfelelő, ha a deklarált workload és failure model mellett teljesíti a
követelményeket. Nincs minden célra optimális database.

## Források

- [NIST CSRC — Database glossary](https://csrc.nist.gov/glossary/term/Database) — tág database-definíció és eredeti NIST-források.
- [PostgreSQL 18 — SQL Concepts](https://www.postgresql.org/docs/18/tutorial-concepts.html) — relational system, table, row, column és row-order viselkedés.
- [IBM Research — Codd 1970](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks) — a relational model és data independence történeti alapja.
