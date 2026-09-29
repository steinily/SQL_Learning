---
schema_version: 1
id: DBKB-TX-0021
title: Exactly-Once Claims
type: comparison
primary_domain: transactions-and-concurrency
secondary_domains: [distributed-systems]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-TX-0020]
related: [DBKB-TX-0019]
aliases: [exactly once processing]
search_keywords: [exactly once, at least once, duplicate effect]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Exactly-once claimet boundary és evidence alapján korlátozza]
---
# Exactly-Once Claims

Az exactly-once állítás mindig meghatározott boundaryre vonatkozik: database transaction, message delivery vagy teljes üzleti side effect. A transport delivery önmagában nem bizonyít exactly-once üzleti hatást.

Írd le a failure window-kat, deduplicationt, replay behavior-t és az evidence-t; ha nincs end-to-end bizonyíték, használj at-least-once + idempotent consumer leírást.

## Források
- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
