---
schema_version: 1
id: DBKB-FND-0029
title: CAP Theorem Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [distributed-systems, consistency]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: []
scope: general
prerequisites: [DBKB-FND-0003, DBKB-FND-0028]
related: [DBKB-FND-0026, DBKB-FND-0031, DBKB-FND-0032]
aliases: [CAP theorem, Brewer conjecture]
search_keywords: [consistency, availability, partition tolerance, linearizability, distributed system]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0001]
source_ids: [SRC-000008]
acceptance_criteria:
  - A Gilbert–Lynch modell definícióival magyarázza a három tulajdonságot.
  - Elutasítja a kontextus nélküli choose-two leegyszerűsítést.
  - Elkülöníti a CAP consistency fogalmát az ACID consistency fogalmától.
---
# CAP Theorem Fundamentals

A **CAP theorem** egy formal impossibility result distributed data services számára. Gilbert
és Lynch 2002-es elsődleges tanulmánya az asynchronous network modelben bizonyítja, hogy a
tanulmány által definiált consistency, availability és partition tolerance guarantee együtt
nem biztosítható.

Ez a mondat csak a definíciókkal együtt pontos. A CAP nem általános termékválasztási szlogen,
és nem azt állítja, hogy egy rendszer teljes életében tetszőlegesen „kiválaszt kettőt”.

## C — Consistency

A tanulmány **atomic consistency** fogalma linearizable data objectet jelent. Az operationök
úgy rendezhetők teljes sorrendbe, mintha mindegyik egyetlen időpillanatban történt volna, és a
real-time orderrel összeegyeztethető eredményt adna.

Ez nem azonos az [ACID](acid.md) `Consistency` betűjével, amely az érvényes state és invariant
megőrzésének transaction-kontekstuként használatos. A „strong consistency” kifejezést is csak
konkrét guarantee megnevezésével érdemes használni: linearizability, serializability és causal
consistency különböző fogalmak.

## A — Availability

A formal model availability követelménye szerint a non-failing node-hoz érkező minden request
response-t kap. Ez erősebb és pontosabb állítás annál, hogy egy szolgáltatásnak magas az éves
uptime százaléka vagy gyors az átlagos response ideje.

A timeout, error vagy „próbáld később” válasz üzletileg lehet kontrollált degradation, de a
formal guarantee értékelésénél nem szabad automatikusan sikeres availabilitynek nevezni.

## P — Partition tolerance

Partition esetén a network két vagy több komponensre szakadhat úgy, hogy a komponensek között
üzenetek vesznek el vagy korlátlanul késnek, miközben a node-ok egy része tovább fut. A
partition tolerance annak követelménye, hogy a rendszer viselkedése a megadott guarantee-k
szerint ilyen communication failure mellett is értelmezett legyen.

Distributed deploymentben a partition nem egyszerűen választható feature: a network failure
lehetőségét a failure modelben kezelni kell. A tényleges engineering döntés partition közben
gyakran az, hogy bizonyos operationök megtagadhatók-e a linearizable consistency megőrzéséért,
vagy stale/conflicting eredmény engedhető-e a response érdekében.

## Mit bizonyít a theorem?

Az asynchronous modelben partition mellett nem lehet egyszerre garantálni a formal atomic
consistencyt és azt, hogy minden request választ kapjon. Intuitív példa: két egymástól elvágott
replica ugyanarról a value-ról nem tud egyszerre friss, közös döntést hozni és minden oldalon
várakozás nélkül válaszolni, ha nem kommunikálhatnak.

A primary paper külön tárgyal partially synchronous modelt és gyengített guarantee-ket is.
Ezért a korrekt elemzés nem áll meg a három betűnél: meg kell nevezni a network assumptiont,
operation típust, consistency modelt, timeoutot, failure detectiont és recovery behavior-t.

## Miért félrevezető a „choose two”?

- Normál, partition nélküli üzemben egy rendszer másképp viselkedhet, mint aktív partition
  alatt.
- Read és write operation eltérő policyt követhet.
- Egyetlen product különböző configuration mellett eltérő guarantee-t adhat.
- Availability és consistency nem egyetlen skála két vége; több, pontosabban definiált modell
  létezik.
- A theorem nem értékeli automatikusan latency, durability, transaction isolation, cost vagy
  operability követelményeit.

## Elemzési sablon

CAP-ra hivatkozáskor válaszold meg:

1. Mi a system boundary és hány independently failing node van?
2. Mit jelent a partition a feltételezett network modelben?
3. Mely operationökre kérünk milyen consistency guarantee-t?
4. Mit számít sikeres response-nak, és van-e határidő?
5. Mi történik partition alatt read, write és coordination esetén?
6. Hogyan történik reconciliation vagy recovery a communication helyreállása után?

Ha ezek hiányoznak, a „CP” vagy „AP” címke kevés a design döntés igazolásához.

## Kapcsolat a database engineeringgel

A CAP analysis különösen multi-node replicated systemnél releváns. Egyetlen process vagy
egyetlen failure domain lokális transaction viselkedését nem magyarázza. Ugyancsak nem
helyettesíti az isolation, consensus, quorum, replication lag vagy backup elemzését. Ezek a
kapcsolódó M30 Distributed Data Systems témákban kapnak részletes kezelést.

## Forrás

- [Seth Gilbert és Nancy Lynch — Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services](https://www.cs.princeton.edu/courses/archive/spring21/cos418/papers/cap.pdf) — az asynchronous model, a három formal property és az impossibility proof elsődleges forrása.
