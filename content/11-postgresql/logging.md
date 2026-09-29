---
schema_version: 1
id: DBKB-PG-0024
title: Logging
type: technology
primary_domain: postgresql
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0004]
related: [DBKB-PG-0025]
aliases: [PostgreSQL logs]
search_keywords: [PostgreSQL logging, log_min_duration_statement, audit log]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Logging signal, volume, privacy és retention trade-offot adja]
---
# Logging

PostgreSQL logging konfigurációval connection, statement, duration, checkpoint és error signal rögzíthető. Query text és parameter érzékeny lehet; verbosity, sampling, retention és access policy együtt tervezendő.

## Források
- [PostgreSQL 18 — Error Reporting and Logging](https://www.postgresql.org/docs/18/runtime-config-logging.html)
