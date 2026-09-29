---
schema_version: 1
id: DBKB-SEC-0002
title: Database Threat Modeling
type: concept
primary_domain: security-privacy
secondary_domains: [risk-management]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0001]
related: []
aliases: [database threat model]
search_keywords: [threat modeling, attack surface, trust boundary, abuse case]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050]
acceptance_criteria: [Assets, threats, boundaries and mitigations are identified]
---
# Database Threat Modeling

Threat model-ben azonosítsd az assets, actors, trust boundaries, data flows és abuse case-eket. A control legyen threat-hez és evidence-hez kötve; generic checklist nem helyettesíti a konkrét deployment, credential, network és data classification elemzését.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
