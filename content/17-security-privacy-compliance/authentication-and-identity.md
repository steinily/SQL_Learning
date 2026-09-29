---
schema_version: 1
id: DBKB-SEC-0003
title: Authentication and Identity
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
prerequisites: [DBKB-SEC-0002]
related: []
aliases: [database authentication]
search_keywords: [authentication, identity provider, MFA, service account]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050]
acceptance_criteria: [Human and service identity controls are scoped]
---
# Authentication and Identity

Authentication policy külön kezelje a human, service és break-glass identity-ket. Használj központi identity source-ot, erős credential lifecycle-t és szükség szerint MFA-t; engine-specific authentication plugin vagy default csak target version és environment ellenőrzése után fogadható el.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
