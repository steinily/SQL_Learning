---
schema_version: 1
id: DBKB-CAP-0016
title: Migration Case Study
type: case-study
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
prerequisites: [DBKB-CAP-0015]
related: [DBKB-MIG-0001]
aliases: [migration case]
search_keywords: [migration, dual write, backfill, cutover, rollback]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Scenario requires migration strategy, compatibility, backfill, cutover and rollback evidence]
---
# Migration Case Study

Egy legacy relational workloadot új platformra migrálnak rövid downtime window-val. Tervezz inventory, expand/contract, CDC/dual-write, backfill, reconciliation, cutover, rollback és decommission lépéseket.

Elvárt evidence: schema/query inventory, lag/watermark, count/checksum/invariant, consumer compatibility és RPO/RTO. A migration success csak actual validation outputtal igazolható.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
