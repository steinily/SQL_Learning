---
schema_version: 1
id: DBKB-MY-0010
title: Stored Programs
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
prerequisites: [DBKB-MY-0007]
related: [DBKB-MY-0011]
aliases: [stored procedure, stored function]
search_keywords: [MySQL stored procedure, stored function, delimiter, handler]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Procedure/function, parameter, handler és transaction behavior scopeját adja]
---
# Stored Programs

MySQL/MariaDB stored procedure és function procedural SQL-t, parameters és condition handlers-t ad. Routine security context, deterministic claim, transaction boundary és deployment delimiter/tooling külön reviewt igényel.

## Források
- [MySQL 8.4 — Stored Object Syntax](https://dev.mysql.com/doc/refman/8.4/en/stored-objects.html)
