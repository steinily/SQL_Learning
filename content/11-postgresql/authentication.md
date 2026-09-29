---
schema_version: 1
id: DBKB-PG-0022
title: Authentication
type: technology
primary_domain: postgresql
secondary_domains: [security]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0020]
related: [DBKB-PG-0023]
aliases: [pg_hba.conf]
search_keywords: [PostgreSQL authentication, pg_hba.conf, scram, peer]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [pg_hba.conf rule matching, method és reload safety témáit adja]
---
# Authentication

PostgreSQL client authentication rules `pg_hba.conf` sorainak sorrendje és methodja alapján választódnak. SCRAM, certificate, peer és trust eltérő security model; rule change előtt test connection, rollback és audit evidence kell.

## Források
- [PostgreSQL 18 — The pg_hba.conf File](https://www.postgresql.org/docs/18/auth-pg-hba-conf.html)
