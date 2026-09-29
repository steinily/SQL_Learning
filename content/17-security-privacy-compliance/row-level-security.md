---
schema_version: 1
id: DBKB-SEC-0009
title: Row Level Security
type: technology
primary_domain: security-privacy
secondary_domains: [authorization]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server]
sql_dialects: [postgresql, tsql]
scope: vendor-specific
prerequisites: [DBKB-SEC-0004]
related: []
aliases: [RLS]
search_keywords: [row-level security, tenant isolation, policy predicate]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050]
acceptance_criteria: [RLS policy scope, bypass paths and testing are identified]
---
# Row Level Security

Row-level security policy a query által látható rows-at predicate alapján korlátozza, de owner, elevated role, bypass setting, views és maintenance paths külön vizsgálandó. Tenant isolation-t negative tests-szel is ellenőrizd, és dokumentáld a policy context source-át.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
