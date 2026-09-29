---
schema_version: 1
id: DBKB-SEC-0006
title: Secrets Management
type: playbook
primary_domain: security-privacy
secondary_domains: [identity, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0003, DBKB-SEC-0005]
related: []
aliases: [database credential management]
search_keywords: [secrets, credential rotation, vault, key material]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050]
acceptance_criteria: [Secret storage, rotation and exposure controls are defined]
---
# Secrets Management

Database credentials, certificates és encryption keys ne kerüljenek source code-ba, image-be vagy logba. Használj dedicated secret store-t, scoped retrieval-t, rotation és revocation folyamatot, valamint audit evidence-et; rotation előtt teszteld a connection failover és application recovery útvonalát.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
