---
schema_version: 1
id: DBKB-MY-0004
title: Databases and Schemas
type: concept
primary_domain: mysql-mariadb
secondary_domains: [schema-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0002]
related: [DBKB-MY-0005]
aliases: [database/schema namespace]
search_keywords: [MySQL database, schema, USE, information_schema]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Database/schema namespace, default database és metadata scopeját adja]
---
# Databases and Schemas

MySQL-ben a `SCHEMA` és `DATABASE` gyakran synonymként jelenik meg, de migration tooling és fork behavior ellenőrzendő. `USE` session state-et változtat; explicit qualification és `information_schema`/catalog scope legyen dokumentált.

## Források
- [MySQL 8.4 — CREATE DATABASE](https://dev.mysql.com/doc/refman/8.4/en/create-database.html)
