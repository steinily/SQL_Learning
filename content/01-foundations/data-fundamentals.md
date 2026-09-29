---
schema_version: 1
id: DBKB-FND-0002
title: Data Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [data-engineering, data-quality]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: []
scope: general
prerequisites: []
related: [DBKB-FND-0003, DBKB-FND-0005, DBKB-FND-0024, DBKB-FND-0033]
aliases: [data, datum, information]
search_keywords: [adat, információ, jelentés, struktúra, metadata, lineage]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0001]
source_ids: [SRC-000001, SRC-000002]
acceptance_criteria:
  - Elkülöníti az adatot a jelentéstől és a fizikai reprezentációtól.
  - Bemutatja a structure, metadata, quality és lifecycle alapfogalmait.
  - A database fogalmához canonical hivatkozást ad.
---
# Data Fundamentals

Az **adat** egy megfigyelés, mérés, esemény vagy állítás rögzített reprezentációja. A
reprezentáció önmagában még nem biztosít helyes értelmezést: a `42` érték jelenthet
darabszámot, hőmérsékletet, azonosítót vagy hibakódot. Használható információ akkor lesz
belőle, ha ismerjük a jelentését, egységét, kontextusát és keletkezésének körülményeit.

Ezért egy data system nem csak értékeket mozgat. Meg kell őriznie vagy hozzáférhetővé kell
tennie azt a kontextust is, amely alapján az érték értelmezhető és felelősen felhasználható.

## Érték, jelentés és reprezentáció

Három réteget érdemes különválasztani:

1. A **valós jelenség** az, amiről tudni szeretnénk valamit, például egy megrendelés.
2. A **logikai adat** a jelenség modellben rögzített állítása, például a megrendelt mennyiség.
3. A **fizikai reprezentáció** a bitek, karakterek, fájlblokkok vagy database page-ek
   formája, amelyekben az állítást tároljuk.

Ugyanaz a logikai adat eltérő fizikai formát kaphat. Egy időpont megjelenhet ISO 8601 text,
integer epoch vagy engine-specifikus `timestamp` formában. A reprezentáció megváltoztatása
nem változtathatja meg csendben a jelentést. A [relational model](relational-model-fundamentals.md)
egyik történeti motivációja éppen a logikai használat és a belső tárolási reprezentáció
szétválasztása volt.

## Structure és schema

A **structure** meghatározza, hogyan tagoljuk az adatot. Egy tabular structure sorokra és
oszlopokra, egy JSON document objectekre és array-ekre, egy event stream pedig időben
rendezett eseményekre épülhet. A **schema** a megengedett structure, név, type és constraint
géppel vagy emberrel olvasható leírása.

A `structured`, `semi-structured` és `unstructured` megnevezés nem minőségi sorrend.
Arra utal, mennyire előre rögzített, illetve hol érvényesül a schema. Egy JSON payloadnak is
lehet szigorú schema-ja, miközben egy táblába importált CSV lehet szemantikailag rendezetlen.

## Metadata és provenance

A **metadata** adat az adatról. Tipikus példák:

- column name, data type és business definition;
- source system és owner;
- létrehozási vagy módosítási idő;
- sensitivity classification;
- transformation rule és lineage;
- érvényességi vagy retention szabály.

A **provenance** azt írja le, honnan származik az adat és milyen lépéseken ment át. A
**lineage** ennek rendszer- és mezőszintű kapcsolati nézete. Provenance nélkül egy helyesnek
tűnő szám sem feltétlenül auditálható vagy reprodukálható.

## Quality nem egyetlen tulajdonság

Az adatminőség mindig célhoz és szabályhoz kötött. Gyakori quality dimension a completeness,
validity, accuracy, consistency, uniqueness és timeliness. Ezek nem következnek egymásból:
egy kitöltött érték lehet pontatlan; egy valid type-pal tárolt országkód lehet üzletileg
ismeretlen; két külön-külön helyes rekord lehet egymás duplikátuma.

A quality rule legyen mérhető. A „jó minőségű customer data” nem végrehajtható feltétel, a
„minden aktív customer rendelkezik kétbetűs country code-dal” viszont ellenőrizhető. A
constraint, validation query és monitoring ugyanazt a business meaninget különböző
életciklus-pontokon védheti.

## Lifecycle és felelősség

Egy gyakorlati data lifecycle tipikus állomásai: capture, ingestion, validation, storage,
transformation, serving, retention és deletion/archive. Minden állomáson más kérdések
dominálnak:

- Capture: mit figyeltünk meg, és milyen pontossággal?
- Ingestion: elveszett, duplikálódott vagy átrendeződött-e valami?
- Storage: milyen schema, constraint és access control védi?
- Transformation: reprodukálható-e, és követhető-e a lineage?
- Serving: ugyanazt jelenti-e a metric minden consumer számára?
- Retention: meddig szükséges és jogszerű megtartani?

Az ownership ezért nem pusztán platformüzemeltetés. A producer felel a jelentés és a
contract közléséért, a platform a megbízható kezelésért, a consumer pedig azért, hogy az
adatot a deklarált korlátokon belül használja.

## Data és database

A database az adat egyik szervezett tárolási és kezelési formája, nem az adat szinonimája.
A NIST tág definíciója szerint database lehet információ- vagy data repository akkor is, ha
nem hagyományos relational rendszer. A részletes fogalmi és rendszerhatárbeli különbséget a
[Database Fundamentals](database-fundamentals.md) tárgyalja.

## Ellenőrző kérdések

- Meg tudod nevezni egy érték unitját, időbeli érvényességét és ownerét?
- Különválasztható a business meaning a konkrét file vagy database representation formától?
- A quality állítás végrehajtható szabállyá alakítható?
- Egy downstream érték visszavezethető a source-ra és a transformation lépésekre?

## Források

- [NIST CSRC — Database glossary](https://csrc.nist.gov/glossary/term/Database) — a database tág, nem kizárólag relational értelmezése.
- [IBM Research — A Relational Model of Data for Large Shared Data Banks](https://research.ibm.com/publications/a-relational-model-of-data-for-large-shared-data-banks) — a logikai és belső reprezentáció szétválasztásának elsődleges történeti forrása.
