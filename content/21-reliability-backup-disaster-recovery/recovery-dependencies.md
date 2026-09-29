---
schema_version: 1
id: DBKB-DR-0010
title: Recovery Dependencies
type: concept
primary_domain: disaster-recovery
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0007]
related: []
aliases: [recovery dependency map]
search_keywords: [dependency order, DNS, identity, storage, key management]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000064]
acceptance_criteria: [Technical, identity, network, key and application dependencies are identified]
---
# Recovery Dependencies

Recovery dependency map tartalmazza a network/DNS, identity, secret/key management, storage, database, application, queue/cache, monitoring és external provider sorrendet. Database restore sikerét nem tekintsd service recoverynek, ha a credential, schema migration, DNS vagy downstream dependency még unavailable.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
