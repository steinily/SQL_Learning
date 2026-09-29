---
schema_version: 1
id: DBKB-MIG-0019
title: Migration Troubleshooting
type: troubleshooting
primary_domain: migration
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0018]
related: []
aliases: [schema migration failure diagnosis]
search_keywords: [migration failure, lock timeout, checksum, drift, partial apply]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Failure classification and evidence-preserving response are described]
---
# Migration Troubleshooting

Migration failuret syntax/compatibility, lock/timeout, data, permission, storage, replication, application contract vagy partial-apply kategóriába sorold. Preserve-eld logs, migration state és transaction evidence-et; retry, manual fix vagy rollback/roll-forward csak explicit state assessment után induljon.

## Források
- [MySQL — ALTER TABLE](https://dev.mysql.com/doc/refman/8.4/en/alter-table.html)
