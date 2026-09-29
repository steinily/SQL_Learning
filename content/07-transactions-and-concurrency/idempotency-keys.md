---
schema_version: 1
id: DBKB-TX-0020
title: Idempotency Keys
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [application-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-TX-0019]
related: [DBKB-TX-0021]
aliases: [idempotency token, request deduplication]
search_keywords: [idempotency key, duplicate request, retry safety]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Unique key, replay behavior és retention policy mintát ad]
---
# Idempotency Keys

Idempotency key segítségével ugyanaz a klienskérés újrafuttatva nem hoz létre több üzleti hatást. Tárold a kulcsot a request fingerprinttel, eredménnyel és expiryvel; a key uniqueness legyen adatbázis constraint.

Az idempotency nem tesz minden side effectet atomicussá: külső hívásnál outbox vagy dedikált reconciliation szükséges.

## Források
- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
