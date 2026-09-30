---
schema_version: 1
id: DBKB-CAP-0039
title: Migration Exercise
type: exercise
primary_domain: capstone
secondary_domains: [migration, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, mysql, apache-kafka]
sql_dialects: [postgresql, mysql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0038]
related: [DBKB-MIG-0001]
aliases: [migration lab]
search_keywords: [migration exercise, backfill, CDC, cutover, rollback]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Learner produces inventory, dual-run, reconciliation, cutover and rollback evidence]
---
# Migration Exercise

Tervezd meg legacy order database staged migrationját: inventory, expand/contract, CDC/dual-write, backfill, compatibility, cutover, rollback és decommission.

Készíts lag/watermark, count/checksum/invariant, consumer sign-off és failure injection tesztet. A migration result csak actual execution outputtal és explicit residual riskkel jelölhető.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
