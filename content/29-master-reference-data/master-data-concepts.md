---
schema_version: 1
id: DBKB-MDM-0002
title: Master Data Concepts
type: concept
primary_domain: master-data
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0001]
related: []
aliases: [master entity]
search_keywords: [master data, customer, product, party, system of record]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Master entity, authoritative source and stewardship concepts are explained]
---
# Master Data Concepts

Master data business entity-ket, például customer, product, supplier vagy location, stabil identityvel és több consumer számára közös semantics-szel kezel. System of record, source precedence, owner, lifecycle, identity resolution és change approval legyen explicit.

## Források
- [ISO 8000](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
