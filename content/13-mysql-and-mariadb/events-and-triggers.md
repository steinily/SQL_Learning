---
schema_version: 1
id: DBKB-MY-0011
title: Events and Triggers
type: technology
primary_domain: mysql-mariadb
secondary_domains: [programming]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0010]
related: [DBKB-MY-0012]
aliases: [event scheduler, trigger]
search_keywords: [MySQL trigger, event scheduler, BEFORE INSERT, AFTER UPDATE]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Trigger timing, event schedule, recursion és hidden side effectet adja]
---
# Events and Triggers

Trigger row eventhez kapcsolódik, event scheduler időalapú routine futtatást adhat. Multi-row statement, execution order, scheduler state, privileges és hidden side effect legyen explicit; idempotency és overlap kontroll szükséges.

## Források
- [MySQL 8.4 — Using Triggers](https://dev.mysql.com/doc/refman/8.4/en/trigger-syntax.html)
