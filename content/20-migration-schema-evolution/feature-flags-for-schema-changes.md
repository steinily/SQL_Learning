---
schema_version: 1
id: DBKB-MIG-0010
title: Feature Flags for Schema Changes
type: technology
primary_domain: migration
secondary_domains: [deployment]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0009]
related: []
aliases: [migration feature flag]
search_keywords: [feature flag, progressive rollout, kill switch, schema path]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000061]
acceptance_criteria: [Flag scope, default, expiry, observability and safety are defined]
---
# Feature Flags for Schema Changes

Feature flag a schema compatibility path rolloutját kontrollálhatja, de flag state, cache, default, expiry, owner és kill-switch semantics legyen. A flag nem oldja meg a DDL lock vagy data parity problémát; old flag path csak usage evidence után távolítható el.

## Források
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/en-us/sql/relational-databases/)
