---
schema_version: 1
id: DBKB-MY-0001
title: MySQL and MariaDB Overview
type: overview
primary_domain: mysql-mariadb
secondary_domains: [database]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-SS-0040]
related: [DBKB-MY-0002, DBKB-MY-0005]
aliases: [MySQL, MariaDB]
search_keywords: [MySQL, MariaDB, InnoDB, SQL mode]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [MySQL/MariaDB fork és version scopeját, közös és eltérő behaviorét összefoglalja]
---
# MySQL and MariaDB Overview

MySQL és MariaDB kapcsolódó, de külön fejlődő relational database rendszerek. SQL syntax, storage engine, optimizer, replication és security feature-ek fork/version szerint eltérhetnek; portability claimhez mindkét official dokumentáció kell.

## Források
- [MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/)
- [MariaDB Server Documentation](https://mariadb.com/kb/en/documentation/)
