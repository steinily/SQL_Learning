---
schema_version: 1
id: DBKB-MY-0028
title: MySQL Anti-Patterns
type: troubleshooting
primary_domain: mysql-mariadb
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0027]
related: [DBKB-MY-0030]
aliases: [MySQL operational anti-pattern]
search_keywords: [MySQL anti-pattern, MyISAM transactions, implicit conversion, no backup test]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Nontransactional engine misuse, mode drift, unbounded connections és restore nélküli backup anti-patternokat adja]
---
# MySQL Anti-Patterns

Kerülendő a nontransactional engine-re atomicity claim, SQL mode drift, wildcard host grants, unbounded connection pool, index nélkül nagy table scan, binlog purge evidence nélkül és restore test nélküli backup claim.

## Források
- [MySQL 8.4 — Optimization](https://dev.mysql.com/doc/refman/8.4/en/optimization.html)
