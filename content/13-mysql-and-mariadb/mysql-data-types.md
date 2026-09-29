---
schema_version: 1
id: DBKB-MY-0007
title: MySQL Data Types
type: reference
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
prerequisites: [DBKB-MY-0006]
related: [DBKB-MY-0008, DBKB-MY-0009]
aliases: [MySQL data types]
search_keywords: [MySQL data types, decimal, varchar, timestamp, conversion]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Numeric, character, temporal, JSON és implicit conversion trade-offot adja]
---
# MySQL Data Types

MySQL/MariaDB data type választás precision, storage, collation, timezone, strict mode és index behavior trade-off. Implicit conversion és display/storage semantics különösen version- és mode-sensitive.

## Források
- [MySQL 8.4 — Data Types](https://dev.mysql.com/doc/refman/8.4/en/data-types.html)
