---
schema_version: 1
id: DBKB-PG-0034
title: PostgreSQL Anti-Patterns
type: troubleshooting
primary_domain: postgresql
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0033]
related: [DBKB-PG-0040]
aliases: [PostgreSQL operational anti-pattern]
search_keywords: [PostgreSQL anti-pattern, superuser app, idle transaction, no vacuum]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Superuser application, disabled vacuum, untested backup és unbounded connection anti-patternokat ad]
---
# PostgreSQL Anti-Patterns

Kerülendő a shared application `SUPERUSER`, trust authentication, unbounded connection pool, disabled autovacuum, backup restore test nélkül és production tuning plan evidence nélkül. Minden kivételnek ownerrel és expiryvel kell rendelkeznie.

## Források
- [PostgreSQL 18 — Secure TCP/IP Connections](https://www.postgresql.org/docs/18/auth-pg-hba-conf.html)
