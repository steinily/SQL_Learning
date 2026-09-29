---
schema_version: 1
id: DBKB-MY-0003
title: Installation and Configuration
type: tutorial
primary_domain: mysql-mariadb
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0001]
related: [DBKB-MY-0006]
aliases: [my.cnf, my.ini]
search_keywords: [MySQL installation, MariaDB installation, my.cnf, server configuration]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Install, initialize, config file, service account, storage és patch scopeját adja]
---
# Installation and Configuration

MySQL/MariaDB telepítésnél package version, data directory, service identity, network bind, authentication, SQL mode és storage policy legyen rögzítve. Production config changehez staged test és rollback kell.

## Források
- [MySQL 8.4 — Installing and Upgrading MySQL](https://dev.mysql.com/doc/refman/8.4/en/installing.html)
- [MariaDB — Installation](https://mariadb.com/kb/en/installation/)
