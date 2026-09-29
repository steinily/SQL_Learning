---
schema_version: 1
id: DBKB-MY-0002
title: MySQL Architecture
type: concept
primary_domain: mysql-mariadb
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql]
sql_dialects: [mysql]
scope: vendor-specific
prerequisites: [DBKB-MY-0001]
related: [DBKB-MY-0013, DBKB-MY-0024]
aliases: [MySQL server architecture]
search_keywords: [MySQL architecture, server, storage engine, client connection]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046]
acceptance_criteria: [Server layer, parser/optimizer, storage engine és client kapcsolatát adja]
---
# MySQL Architecture

MySQL server SQL layerétől a storage engine rétegig különül el; InnoDB tipikus transactional engine, de engine choice behaviort változtat. Connection, parser, optimizer, transaction és engine evidence legyen különválasztva.

## Források
- [MySQL 8.4 — MySQL Server Architecture](https://dev.mysql.com/doc/refman/8.4/en/architecture.html)
