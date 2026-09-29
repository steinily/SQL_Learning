---
schema_version: 1
id: DBKB-PG-0017
title: Triggers
type: technology
primary_domain: postgresql
secondary_domains: [data-integrity]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0016]
related: [DBKB-PG-0018]
aliases: [trigger function]
search_keywords: [PostgreSQL trigger, BEFORE trigger, AFTER trigger, transition table]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Trigger timing/order, recursion és hidden side effect kockázatát adja]
---
# Triggers

Trigger INSERT/UPDATE/DELETE vagy event művelethez kapcsolódó implicit routine invocation. Timing, firing order, recursion, transaction scope és hidden write side effect miatt trigger behavior legyen dokumentált és tesztelt.

## Források
- [PostgreSQL 18 — CREATE TRIGGER](https://www.postgresql.org/docs/18/sql-createtrigger.html)
