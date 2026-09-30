---
schema_version: 1
id: DBKB-REC-0044
title: Security Anti-Patterns
type: error
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
prerequisites: [DBKB-REC-0043]
related: [DBKB-SEC-0001]
aliases: [database security mistakes]
search_keywords: [shared admin, plaintext secret, broad grant, public endpoint, missing audit]
risk: security-sensitive
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Security anti-patterns include detection, containment and corrective control]
---
# Security Anti-Patterns

Anti-pattern a shared admin/service identity, broad permanent grant, plaintext secret/log, public database endpoint, disabled TLS, unrotated key, missing audit és sensitive data unmasked non-productionban.

Detectáld IAM/access review, network scan, secret scanner, audit gap és configuration baseline alapján. Containment revoke/rotate/isolate; recovery után least privilege, encryption, audit and negative access test evidence kell.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
