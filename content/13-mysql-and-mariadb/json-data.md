---
schema_version: 1
id: DBKB-MY-0008
title: JSON Data
type: technology
primary_domain: mysql-mariadb
secondary_domains: [data-modeling]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0007]
related: [DBKB-MY-0014]
aliases: [MySQL JSON]
search_keywords: [MySQL JSON, JSON_TABLE, generated column, JSON path]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [JSON document, path, indexing és schema governance trade-offot adja]
---
# JSON Data

MySQL és MariaDB JSON capabilityjei version/fork szerint eltérhetnek. JSON path, validation, generated column és indexelés használatakor a flexible shape ne rejtse el a relational invariantokat.

## Források
- [MySQL 8.4 — JSON Data Type](https://dev.mysql.com/doc/refman/8.4/en/json.html)
- [MariaDB — JSON](https://mariadb.com/kb/en/json-data-type/)
