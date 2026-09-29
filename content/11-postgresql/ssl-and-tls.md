---
schema_version: 1
id: DBKB-PG-0023
title: SSL and TLS
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
prerequisites: [DBKB-PG-0022]
related: [DBKB-PG-0024]
aliases: [PostgreSQL TLS]
search_keywords: [PostgreSQL SSL, TLS, certificate, sslmode]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [TLS encryption, certificate validation és sslmode policyt dokumentálja]
---
# SSL and TLS

TLS encrypts client/server transportot, de certificate validation nélkül MITM risk maradhat. `sslmode`, CA, hostname verification, certificate rotation és client compatibility legyen explicit és tesztelt.

## Források
- [PostgreSQL 18 — SSL/TLS](https://www.postgresql.org/docs/18/ssl-tcp.html)
