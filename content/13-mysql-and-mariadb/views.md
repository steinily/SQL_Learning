---
schema_version: 1
id: DBKB-MY-0012
title: Views
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
prerequisites: [DBKB-MY-0004]
related: [DBKB-MY-0010]
aliases: [CREATE VIEW]
search_keywords: [MySQL view, updatable view, algorithm merge temptable]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [View algorithm, updatability, security és dependency behaviorét adja]
---
# Views

MySQL/MariaDB view query abstractiont és security boundaryt ad; `ALGORITHM` és updatability behavior query shape/version függő. View nem automatikusan materialized, ezért freshness és performance claim külön bizonyítandó.

## Források
- [MySQL 8.4 — Views](https://dev.mysql.com/doc/refman/8.4/en/views.html)
