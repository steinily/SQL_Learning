---
schema_version: 1
id: DBKB-REC-0034
title: Permission Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [security, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0033]
related: [DBKB-SEC-0001]
aliases: [database authorization runbook]
search_keywords: [permission denied, GRANT, role, ownership, policy, auth]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Principal, inheritance, object, policy, network and audit diagnosis are actionable]
---
# Permission Troubleshooting

Capture principal/service identity, auth method, database/schema/object, action, role inheritance, ownership, row/column policy, network source és exact error. Reproduce with least-privilege test identity, not with admin escalation.

Fix additive, scoped grant vagy policy correction legyen expiry/audit mellett. Verify-old positive és negative access, cache/session refresh, audit event és downstream consumer; broad grant és shared credential tilos workaroundként.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
