---
schema_version: 1
id: DBKB-TX-0011
title: Blocking and Lock Waits
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
prerequisites: [DBKB-TX-0009, DBKB-TX-0010]
related: [DBKB-TX-0012, DBKB-TX-0023]
aliases: [blocked session, lock wait]
search_keywords: [blocking, lock wait, blocked transaction]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Blocker és blocked session diagnosztikai folyamatot ad bizonyíték nélkül claim nélkül]
---
# Blocking and Lock Waits

Diagnózis: azonosítsd a várakozó sessiont, a blocker sessiont, a lockolt objektumot, a transaction age-et és a query textet. A remediation legyen ownership-alapú: előbb query- és transaction-boundary okot keress, csak utána avatkozz be.

Production incidentben a snapshotot időbélyeggel és azonosítókkal mentsd; a pillanatnyi monitoring nézet nem bizonyítja a korábbi állapotot.

## Források

- [PostgreSQL 18 — Explicit Locking](https://www.postgresql.org/docs/18/explicit-locking.html)
