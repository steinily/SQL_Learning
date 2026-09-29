---
schema_version: 1
id: DBKB-DR-0016
title: Recovery Governance
type: playbook
primary_domain: disaster-recovery
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0015]
related: []
aliases: [DR governance]
search_keywords: [recovery owner, approval, exception, exercise cadence]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000064]
acceptance_criteria: [Ownership, review cadence, exceptions and plan maintenance are specified]
---
# Recovery Governance

Recovery governance-ban business owner, service owner, technical recovery owner, communications, approval authority, exercise cadence, exception expiry és plan review date szerepeljen. Plan csak akkor aktuális, ha dependency, contact, artifact location és actual test evidence frissítve van.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
