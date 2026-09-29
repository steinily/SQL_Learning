---
schema_version: 1
id: DBKB-REC-0009
title: Security Recipes
type: playbook
primary_domain: recipes
secondary_domains: [security, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0008]
related: [DBKB-SEC-0001]
aliases: [database security runbook]
search_keywords: [GRANT, role, TLS, masking, audit, secret rotation]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [Least privilege, grants, encryption, masking, audit and revocation are covered]
---
# Security Recipes

Security recipeben inventoryzd principal/resource/action/data classificationt, majd least-privilege role-t adj; human, service és break-glass identityt különítsd el. Grant változás legyen peer-reviewed, expiryvel és audit loggal.

TLS/mTLS, encryption-at-rest, key rotation, secret redaction, row/column masking és export control legyen verified control. Revoke és incident testben ellenőrizd a cache/session/replica propagationt; broad admin grant ne legyen tartós workaround.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
