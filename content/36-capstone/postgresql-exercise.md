---
schema_version: 1
id: DBKB-CAP-0028
title: PostgreSQL Exercise
type: exercise
primary_domain: capstone
secondary_domains: [postgresql, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-CAP-0027]
related: [DBKB-PG-0001]
aliases: [PostgreSQL lab]
search_keywords: [PostgreSQL exercise, EXPLAIN, VACUUM, replication, backup]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner runs PostgreSQL plan, maintenance, backup and replication checks]
---
# PostgreSQL Exercise

Készíts reproducible PostgreSQL labot: schema/seed, slow query baseline, index/plan change, maintenance check, backup/restore és replication health check.

Rögzítsd PostgreSQL version/configot, commands, outputot, expected resultot és cleanupot. Unsupported production-only feature vagy benchmark ne kerüljön execution-verified státuszba.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
