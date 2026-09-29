---
schema_version: 1
id: DBKB-RDBE-0011
title: Partition Keys and Boundaries
type: concept
primary_domain: relational-database-engineering
secondary_domains: [data-modeling, operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-RDBE-0010, DBKB-FND-0015]
related: [DBKB-ASQL-0021]
aliases: [partition boundary design]
search_keywords: [partition key, range boundary, list value, default partition]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000038]
acceptance_criteria: [Half-open boundary és timezone risket kezeli, Future partition workflow-t ad]
---
# Partition Keys and Boundaries

Range partition boundary legyen explicit, jellemzően half-open `[from,to)`, hogy adjacent partitionök
ne fedjék egymást. Temporal key-nél timezone, precision, late event és future boundary provisioning
része a designnak.

List partitionnél unknown code/default policy, hash partitionnél distribution és rebalancing kérdés
áll fenn. Partition key update row movementet vagy failure-t okozhat. Every boundary change legyen
rehearsed migration és monitoringgal védve.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
- [PostgreSQL 18 — Date/Time Types](https://www.postgresql.org/docs/18/datatype-datetime.html)
