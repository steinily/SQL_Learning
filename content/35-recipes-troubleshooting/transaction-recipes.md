---
schema_version: 1
id: DBKB-REC-0005
title: Transaction Recipes
type: playbook
primary_domain: recipes
secondary_domains: [sql, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0004]
related: [DBKB-TX-0001]
aliases: [transaction runbook]
search_keywords: [BEGIN, COMMIT, ROLLBACK, isolation, deadlock, retry]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [Transaction boundary, isolation, timeout, retry, deadlock and evidence controls are defined]
---
# Transaction Recipes

Transaction scope, isolation, timeout, lock order és retry policy legyen explicit. Keep transaction short, deterministic és idempotent; external API callt ne tarts nyitott DB transactionben, ha elkerülhető.

Deadlock/serialization failure esetén bounded retry csak safe/idempotent operationre, jitterrel és observabilityvel használható. Commit/rollback után verify-old business invariantot és audit eventet; dialect-specific isolation semantics-et official docs alapján ellenőrizd.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
