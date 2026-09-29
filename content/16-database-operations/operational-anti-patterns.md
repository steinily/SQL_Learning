---
schema_version: 1
id: DBKB-OPS-0019
title: Operational Anti-Patterns
type: troubleshooting
primary_domain: database-operations
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0013]
related: []
aliases: [DBA anti-patterns]
search_keywords: [manual production change, untested restore, configuration drift]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Common unsafe practices and corrective controls are listed]
---
# Operational Anti-Patterns

Kerülendő a productionben dokumentálatlan manual change, a backup restore test nélküli elfogadása, a privilege broadening review nélkül, a limitless retry és a configuration drift figyelmen kívül hagyása. Minden anti-patternhez mérhető control és owner tartozzon.

## Források
- [PostgreSQL — Server Administration](https://www.postgresql.org/docs/current/admin.html)
