---
schema_version: 1
id: DBKB-MY-0017
title: Transactions
type: concept
primary_domain: mysql-mariadb
secondary_domains: [concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0013]
related: [DBKB-MY-0018]
aliases: [START TRANSACTION, COMMIT, ROLLBACK]
search_keywords: [MySQL transaction, autocommit, savepoint, rollback]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Autocommit, explicit boundary, savepoint és engine scopeját adja]
---
# Transactions

MySQL/MariaDB transaction behavior storage engine és autocommit setting függő. `START TRANSACTION`, `COMMIT`, `ROLLBACK` és savepoint boundaryt explicit kezeld; nontransactional engine műveletei nem ugyanazt az atomicity contractot adják.

## Források
- [MySQL 8.4 — START TRANSACTION](https://dev.mysql.com/doc/refman/8.4/en/commit.html)
