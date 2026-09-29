---
schema_version: 1
id: DBKB-TX-0019
title: Retryable Errors
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [application-design]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0012]
related: [DBKB-TX-0020, DBKB-TX-0021]
aliases: [transaction retry, serialization failure]
search_keywords: [retryable error, serialization failure, deadlock retry]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Retry classification, backoff és idempotency feltételeit megadja]
---
# Retryable Errors

Retry csak explicit error classification után történjen. Serialization failure vagy deadlock victim újrapróbálható lehet, de a teljes transactiont kell újraindítani, bounded exponential backoff-fal és attempt limitettel.

Nem retryable minden timeout vagy constraint violation; a döntést SQLSTATE és üzleti idempotency alapján dokumentáld.

## Források
- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
