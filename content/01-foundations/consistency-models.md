---
schema_version: 1
id: DBKB-FND-0028
title: Consistency Models
type: concept
primary_domain: foundations
secondary_domains: [distributed-systems, transactions]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [azure-cosmos-db]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-FND-0025, DBKB-FND-0027]
related: [DBKB-FND-0026, DBKB-FND-0029]
aliases: [strong consistency, eventual consistency, session consistency]
search_keywords: [linearizability, staleness, read-your-writes, ordering, replica]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-FND-0004]
source_ids: [SRC-000018, SRC-000008]
acceptance_criteria:
  - Konkrét guarantee-ként kezeli a consistency modelt.
  - Elkülöníti a transaction isolation és CAP fogalmaktól.
  - Vendor modellt csak deklarált contextben használ példának.
---
# Consistency Models

A **consistency model** azt írja le, milyen orderinget és freshness guarantee-t lát a consumer
concurrent vagy replicated operationök mellett. A „consistent” jelző önmagában nem elég;
nevezd meg a modelt, scope-ot és operationt.

## Gyakori guarantee-k

- **Linearizability/strong:** operationök real-time sorrenddel összeegyeztethető egyetlen
  instant hatású orderbe rendezhetők.
- **Sequential consistency:** közös order van, de nem feltétlenül tartja a real-time ordert.
- **Causal consistency:** causally related operationök orderje megmarad.
- **Session guarantees:** read-your-writes, monotonic read/write vagy writes-follow-reads egy
  session scope-jában.
- **Bounded staleness:** verzió- vagy időkorláttal enged régi readet.
- **Eventual consistency:** write hiányában a replica-k idővel konvergálnak; intermediate
  freshness/order külön guarantee nélkül gyenge lehet.

Azure Cosmos DB current official dokumentációja strong, bounded staleness, session, consistent
prefix és eventual szinteket definiál. Ez concrete product model, nem univerzális ötös taxonomy.

## Nem ugyanazok a fogalmak

ACID consistency invariant-preserving transaction fogalom. Isolation a concurrent transaction
láthatóságát és anomaly-jait szabályozza. CAP consistency a Gilbert–Lynch paper atomic/
linearizable object guarantee-je. Ezek kapcsolatban állnak, de nem csereszabatosak.

## Contract kérdések

- Egy key, partition, session vagy teljes database a scope?
- Read után milyen write láthatóság szükséges?
- Mekkora staleness elfogadható időben vagy verzióban?
- Failure/partition alatt error, wait vagy stale result a policy?
- Reconciliation után milyen conflict resolution történik?

## Források

- [Azure Cosmos DB — Consistency levels](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels)
- [Gilbert–Lynch CAP paper](https://www.cs.princeton.edu/courses/archive/spring21/cos418/papers/cap.pdf)
