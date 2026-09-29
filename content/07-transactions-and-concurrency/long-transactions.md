---
schema_version: 1
id: DBKB-TX-0022
title: Long Transactions
type: troubleshooting
primary_domain: transactions-and-concurrency
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0013, DBKB-TX-0017]
related: [DBKB-TX-0018, DBKB-TX-0023]
aliases: [idle in transaction, long-running transaction]
search_keywords: [long transaction, vacuum horizon, idle in transaction]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Long transaction operational riskjeit és remediationjét felsorolja]
---
# Long Transactions

Hosszú vagy `idle in transaction` állapotú transaction lockot, snapshotot és cleanup pressure-t tarthat fenn. Monitorozd transaction age-et, idle durationt, blocker kapcsolatokat és a kapcsolódó storage metrikákat.

Remediation: rövidítsd a boundaryt, zárd le a hibás sessiont kontrolláltan, és állíts be application timeoutot. Production változtatás előtt incident evidence szükséges.

## Források
- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
