---
schema_version: 1
id: DBKB-INTG-0006
title: Change Data Capture
type: technology
primary_domain: data-integration
secondary_domains: [databases]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [debezium, apache-kafka, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0005]
related: []
aliases: [CDC]
search_keywords: [change data capture, snapshot, offset, tombstone, schema change]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000070]
acceptance_criteria: [Snapshot, log position, event envelope, deletes and schema changes are covered]
---
# Change Data Capture

CDC source database change logját snapshot és incremental event stream formában továbbíthatja. Snapshot mode, offset, transaction/order metadata, delete/tombstone, schema change, retention és connector restart semantics target Debezium/source versionen ellenőrzendő; duplicate vagy gap reconciliation kell.

## Források
- [Debezium Documentation](https://debezium.io/documentation/)
