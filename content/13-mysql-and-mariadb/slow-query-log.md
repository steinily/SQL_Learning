---
schema_version: 1
id: DBKB-MY-0025
title: Slow Query Log
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
prerequisites: [DBKB-MY-0024]
related: [DBKB-MY-0027]
aliases: [slow query log]
search_keywords: [MySQL slow query log, long_query_time, log queries]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Threshold, sampling, privacy, rotation és query triage scopeját adja]
---
# Slow Query Log

Slow query log threshold és sampling alapján rögzít queryket; túl alacsony küszöb log volume/PII risket, túl magas küszöb missed signal-t okoz. Rotation, retention, fingerprinting és EXPLAIN follow-up legyen policy.

## Források
- [MySQL 8.4 — Slow Query Log](https://dev.mysql.com/doc/refman/8.4/en/slow-query-log.html)
