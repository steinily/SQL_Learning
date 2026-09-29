---
schema_version: 1
id: DBKB-FND-0027
title: Concurrency Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [transactions, performance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-FND-0025, DBKB-FND-0026]
related: [DBKB-FND-0028, DBKB-FND-0031]
aliases: [concurrent transactions, locking, MVCC]
search_keywords: [isolation, anomaly, blocking, deadlock, retry]
risk: production-critical
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0004]
source_ids: [SRC-000014]
acceptance_criteria:
  - Bemutatja a concurrent access célját és fő anomaly family-ket.
  - Elkülöníti a lock és MVCC mechanizmust a guarantee-tól.
  - Kezeli a deadlock és retry application responsibilityt.
---
# Concurrency Fundamentals

**Concurrency** esetén több session vagy transaction időben átfedve használja ugyanazt az
adatot. A cél nem pusztán párhuzamosság: helyes integrity mellett kell elfogadható throughputot
és latencyt adni.

## Lehetséges anomaly

- **Lost update:** egyik write felülírja a másik változását.
- **Dirty read:** nem committed state látható.
- **Non-repeatable read:** ugyanaz a row újraolvasva megváltozik.
- **Phantom:** ugyanaz a predicate más row-készletet ad.
- **Write skew/serialization anomaly:** külön row-kon végzett write-ok együtt sértenek invariantot.

Az isolation level azt szabályozza, mely jelenség engedett. A név önmagában nem elég: engine
implementation és version is kell.

## Mechanizmusok

Lock konfliktus esetén blockingot vagy deadlockot okozhat. MVCC több row versionnel csökkentheti
reader/writer blockingot. Egyik mechanizmus sem guarantee-név; a látható semanticsot isolation,
statement és engine adja.

## Deadlock és retry

Deadlockban transactionök ciklikusan várnak; a DBMS tipikusan victimet választ és hibával
megszakítja. Az application a teljes transactiont újraindíthatja, ha az operation idempotent és
az error retryable. Retrynak limit, backoff és observability kell.

## Tervezési kérdések

- Mely row/predicate védi az invariantot?
- Optimistic version check vagy pessimistic lock megfelelő?
- Milyen orderben veszünk lockot?
- Mekkora a transaction és mennyi ideig tart user/network wait?
- A retry ismétel-e external side effectet?

## Forrás

- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
