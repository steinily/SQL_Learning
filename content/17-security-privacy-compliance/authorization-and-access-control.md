---
schema_version: 1
id: DBKB-SEC-0004
title: Authorization and Access Control
type: technology
primary_domain: security-privacy
secondary_domains: [identity]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0003]
related: []
aliases: [database authorization]
search_keywords: [authorization, grant, deny, role hierarchy]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050]
acceptance_criteria: [Authorization model and review evidence are explained]
---
# Authorization and Access Control

Authorizationban különítsd el a role assignment, object privilege, administrative privilege és data-level restriction rétegeit. Effective access review ne csak deklarált grants-et, hanem inherited roles-t, ownership-et, application paths-t és emergency access-t is tartalmazzon.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
