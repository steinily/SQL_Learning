---
schema_version: 1
id: DBKB-TX-0008
title: Write Anomalies
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0006, DBKB-TX-0007]
related: [DBKB-TX-0009, DBKB-TX-0015]
aliases: [lost update, write skew]
search_keywords: [write anomaly, lost update, write skew]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Lost update és write skew példákat timeline-ként, isolation scope-pal magyaráz]
---
# Write Anomalies

A lost update akkor keletkezik, amikor két tranzakció ugyanazon korábbi értékre építve ír, és az egyik módosítás elveszik. Write skew esetén külön sorok módosítása sérti a több sorra vonatkozó invariánst. A reprodukcióhoz legalább két session, pontos isolation és commit-sorrend szükséges.

PostgreSQL-ben a dokumentált isolation és row-version visibility szabályok alapján kell megítélni, hogy az adott anomaly engedélyezett-e. Egyetlen session eredménye nem concurrency bizonyíték.

## Források

- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
