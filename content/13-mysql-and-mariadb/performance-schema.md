---
schema_version: 1
id: DBKB-MY-0024
title: Performance Schema
type: technology
primary_domain: mysql-mariadb
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0020]
related: [DBKB-MY-0026]
aliases: [performance_schema]
search_keywords: [MySQL Performance Schema, instrumentation, waits, stages]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Instrumentation, consumers, waits, stages és overhead scopeját adja]
---
# Performance Schema

Performance Schema instrumentációt és event historyt ad statement, wait, stage és transaction observabilityhez. Instrumentation/consumer enablement overheadot és retentiont okozhat; collection policy legyen célzott.

## Források
- [MySQL 8.4 — Performance Schema](https://dev.mysql.com/doc/refman/8.4/en/performance-schema.html)
