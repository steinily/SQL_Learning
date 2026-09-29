---
schema_version: 1
id: DBKB-MY-0009
title: Temporal Data Types
type: technology
primary_domain: mysql-mariadb
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0007]
related: [DBKB-MY-0015]
aliases: [DATETIME, TIMESTAMP, timezone]
search_keywords: [MySQL datetime, timestamp, timezone, temporal type]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Date/time storage, timezone conversion és zero-date mode caveat-et adja]
---
# Temporal Data Types

`DATETIME` és `TIMESTAMP` tárolási/conversion behavior timezone és SQL mode függő lehet. Instant, local wall-clock, precision és invalid-date handling explicit contract legyen.

## Források
- [MySQL 8.4 — Date and Time Data Types](https://dev.mysql.com/doc/refman/8.4/en/date-and-time-types.html)
