---
schema_version: 1
id: DBKB-FND-0004
title: Database Management Systems
type: concept
primary_domain: foundations
secondary_domains: [database-engineering, operations]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: []
scope: general
prerequisites: [DBKB-FND-0003]
related: [DBKB-FND-0005, DBKB-FND-0025, DBKB-FND-0031, DBKB-FND-0034]
aliases: [DBMS, RDBMS, database engine]
search_keywords: [query processor, storage manager, transaction manager, catalog, recovery]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0002]
source_ids: [SRC-000003, SRC-000023]
acceptance_criteria:
  - Meghatározza a DBMS határát és fő komponens-felelősségeit.
  - Elkülöníti a DBMS, database, server instance és client szerepét.
  - Nem állít egységes belső architektúrát minden termékre.
---
# Database Management Systems

A **Database Management System (DBMS)** software-rendszer, amely adatstruktúrák definiálását,
adatok olvasását és módosítását, hozzáférés-szabályozást, concurrencyt és recoveryt biztosít.
Relational modelre épülő változata az **RDBMS**. A DBMS nem azonos sem az adatokkal, sem az
alkalmazással, amely használja.

## Felelősségi területek

- A **parser/binder** értelmezi a statementet és feloldja az object neveket, type-okat.
- A **planner/optimizer** lehetséges execution stratégiák közül választ.
- Az **executor** végrehajtja a tervet, row-kat olvas vagy módosít.
- A **storage manager** page-eket, file-okat, cache-t és access methodokat kezel.
- A **transaction/concurrency subsystem** transaction boundaryt, visibilityt és konfliktust kezel.
- A **recovery subsystem** log és checkpoint alapján segít helyreállítani a declared state-et.
- A **catalog** schema metadatát és belső bookkeeping információt tárol.
- A **security subsystem** authentication, authorization és audit capabilityt ad.

Ez fogalmi bontás. Egy konkrét engine a komponenseket összevonhatja, külön processzekbe
szervezheti vagy service-ek között oszthatja el.

## Rendszerhatárok

A client driver connectiont hoz létre és protocolon keresztül statementet küld. A server
session state-et tarthat, transactiont nyithat és resultot adhat vissza. Connection pool,
proxy, cache és ORM további réteg, de nem feltétlenül a DBMS része.

Vendor terminology eltér. PostgreSQL 18-ban a hierarchy cluster → database → schema → object;
egy connection egy database-hez kapcsolódik. Más termékben az „instance”, „database” és
„schema” eltérő határt jelenthet, ezért deployment leírásban mindig legyen engine és version.

## Declarative interface és physical freedom

SQL használatakor a caller többnyire a kívánt resultot írja le. Az optimizer a schema,
constraint, statistics és resource state alapján választ execution plant. Ez teszi lehetővé,
hogy index vagy storage layout változzon az application statement átírása nélkül. A szabadság
nem korlátlan: type, transaction semantics vagy visible schema módosítása contract change.

## Capability nem guarantee

Az, hogy egy DBMS támogat transactiont, replicationt vagy encryptiont, még nem bizonyítja,
hogy az adott deployment a kívánt guarantee-t nyújtja. Ellenőrizni kell a configurationt,
failure modelt, scope-ot és tesztelt recovery eljárást. Ugyanezért a product category nem
helyettesíti a workload és requirement elemzést.

## Források

- [PostgreSQL 18 — SQL Concepts](https://www.postgresql.org/docs/18/tutorial-concepts.html)
- [PostgreSQL 18 — Glossary](https://www.postgresql.org/docs/18/glossary.html)
