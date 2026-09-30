---
schema_version: 1
id: DBKB-CAP-0052
title: Reference Transactions
type: reference
primary_domain: capstone
secondary_domains: [transactions, reliability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-CAP-0051]
related: [DBKB-TX-0001]
aliases: [transaction checklist]
search_keywords: [transaction reference, ACID, isolation, lock, deadlock, retry]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Transaction boundary, isolation, failure, retry and evidence checklist is provided]
---
# Reference Transactions

Checklist: invariant; transaction boundary; isolation; lock order; timeout; deadlock/serialization behavior; idempotency; retry/backoff; external side effect; commit/rollback; audit; post-check; recovery.

Dialect semantics differ. Before production change, run representative concurrency/failure tests and retain plan, lock graph, output and reviewer evidence.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
