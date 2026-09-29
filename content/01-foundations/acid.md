---
schema_version: 1
id: DBKB-FND-0026
title: ACID
type: concept
primary_domain: foundations
secondary_domains: [transactions, reliability]
levels: [beginner, intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0003, DBKB-FND-0025]
related: [DBKB-FND-0024, DBKB-FND-0027, DBKB-FND-0028, DBKB-FND-0029]
aliases: [Atomicity Consistency Isolation Durability, ACID properties]
search_keywords: [transaction, atomicity, consistency, isolation, durability, commit, rollback]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0001]
source_ids: [SRC-000006, SRC-000007, SRC-000008]
acceptance_criteria:
  - Pontosan elkülöníti az ACID négy tulajdonságát.
  - Nem azonosítja az ACID consistency fogalmát a CAP consistency fogalmával.
  - Bemutatja a guarantee, configuration és application responsibility határát.
---
# ACID

Az **ACID** négy transaction property rövidítése: **Atomicity, Consistency, Isolation,
Durability**. Az IBM official transaction dokumentációja ugyanezt a négyes felosztást adja;
a PostgreSQL 18 transaction tutorial pedig konkrétan bemutatja az all-or-nothing effectet,
visibility boundary-t, `BEGIN`/`COMMIT`/`ROLLBACK` működést és a tartós commit célját.

Az ACID nem egyszerű „van/nincs” címke. A tényleges guarantee az engine, version,
configuration, isolation level, storage és application protocol együttese.

## Atomicity

Egy transaction módosításai egy logikai egységet alkotnak: mind érvényre jutnak, vagy egyik
sem. Ha a transaction `ROLLBACK` outcome-mal zárul, részleges database state nem maradhat
hátra a transactionből.

```sql
BEGIN;
UPDATE account SET balance = balance - 100 WHERE account_id = 1;
UPDATE account SET balance = balance + 100 WHERE account_id = 2;
COMMIT;
```

Atomicity nem jelenti azt, hogy egy külső email, HTTP request vagy file write automatikusan
visszagörgethető. Database-en kívüli side effecthez külön coordination, idempotency vagy
outbox pattern szükséges.

## Consistency

Consistency azt a célt fejezi ki, hogy a transaction egy érvényes database state-ből egy másik
érvényes state-be vigye a rendszert. A DBMS a deklarált type, constraint és transaction
szabályokat tudja kikényszeríteni. A nem deklarált business invariantért az application és a
schema design együtt felel.

Ha például a `balance >= 0` szabály nincs constraintben vagy megfelelő concurrency protocolban
rögzítve, az „ACID database” címke nem találja ki ezt a követelményt. Consistency ezért nem
mentesít a helyes domain modeling és input validation alól.

Ez a **consistency nem azonos a CAP consistency fogalmával**. A formal CAP-tanulmány atomic,
azaz linearizable data-object viselkedést definiál. A két szó kontextus nélküli felcserélése
fogalmi hiba.

## Isolation

Isolation szabályozza, mit láthatnak egymás intermediate state-jéből a concurrent
transactionök, és milyen összhatás engedett. Nem minden isolation level nyújt serializable
viselkedést. Dirty read, non-repeatable read, phantom vagy serialization anomaly lehetősége
engine- és isolation-level-függő.

A magasabb isolation erősebb guarantee-t adhat, de több retryt, blockingot vagy overheadet is
okozhat. Az alkalmazásnak kezelnie kell a dokumentált retryable conflictokat; egy transaction
failure vak ismétlése non-idempotent külső side effect mellett veszélyes.

## Durability

Durability szerint a sikeresen committed és visszaigazolt transaction eredménye túléli a
deklarált failure-eket. A „deklarált” szó lényeges. A guarantee függhet például:

- synchronous vagy asynchronous log flush beállítástól;
- local disk, replicated storage vagy quorum acknowledgement használatától;
- hardware és filesystem failure modeltől;
- backup/restore és disaster-recovery határtól.

Durability nem jelent automatikus védelmet operator error, rossz `DELETE`, credential
compromise vagy region-wide loss ellen. Ezekhez backup, PITR, access control és DR terv kell.

## Ténylegesen futtatott példa

A `SQL-FND-0003` izolált SQLite fixture-ben két accountot hoz létre, transactiont indít, majd
egy constraintet sértő második update-et idéz elő. A harness az expected error classt és a
rollback utáni változatlan balance-okat ellenőrzi. Ez execution evidence az atomic rollback
adott környezetbeli példájára; nem bizonyít általános cross-engine durability vagy isolation
garanciát.

## Ellenőrzőlista

- Hol kezdődik és végződik a business transaction?
- Mely invariantok vannak valóban constrainttel védve?
- Milyen isolation level aktív, és milyen anomaly maradhat lehetséges?
- Milyen error esetén kell a teljes transactiont újrakezdeni?
- Pontosan milyen failure modelre vonatkozik a durability guarantee?
- Vannak database-en kívüli side effectek, amelyek nem rollbackelhetők?

## Források

- [IBM — ACID properties of transactions](https://www.ibm.com/docs/en/cics-tx/11.1.0?topic=processing-acid-properties-transactions) — a négy property official definíciója.
- [PostgreSQL 18 — Transactions](https://www.postgresql.org/docs/18/tutorial-transactions.html) — atomicity, visibility, durability és transaction control concrete leírása.
- [Gilbert–Lynch — CAP primary paper](https://www.cs.princeton.edu/courses/archive/spring21/cos418/papers/cap.pdf) — a CAP consistency eltérő, formal kontextusa.
