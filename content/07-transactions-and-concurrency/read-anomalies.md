---
schema_version: 1
id: DBKB-TX-0007
title: Read Anomalies
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
prerequisites: [DBKB-TX-0006]
related: [DBKB-TX-0008, DBKB-TX-0013]
aliases: [dirty read, nonrepeatable read, phantom]
search_keywords: [read anomaly, dirty read, phantom, nonrepeatable]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Read anomalykat sequence-ként mutatja, Isolation-dependent claimet engine scope-pal ad]
---
# Read Anomalies

Dirty read uncommitted stateet lát; nonrepeatable read ugyanazon row eltérő értékét; phantom read
ugyanazon predicate új/eltűnt row-ját jelenti. Snapshot/MVCC engine-ek ezeket eltérően kezelik.

Anomaly analysis két vagy több session timeline-ja: actor, statement, commit/rollback és visible
result. Egy single-session test nem concurrency evidence. Production claimhez actual multi-session
runtime és configured isolation kell.

## Források

- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
