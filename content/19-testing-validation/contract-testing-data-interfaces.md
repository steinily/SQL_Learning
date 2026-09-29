---
schema_version: 1
id: DBKB-TEST-0008
title: Contract Testing Data Interfaces
type: technology
primary_domain: testing-validation
secondary_domains: [data-contracts]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0007]
related: []
aliases: [data contract tests]
search_keywords: [contract test, producer consumer, schema compatibility, interface]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000059]
acceptance_criteria: [Producer/consumer contract and compatibility assertions are defined]
---
# Contract Testing Data Interfaces

Contract test a producer és consumer között rögzített schema, nullability, type, semantics, ordering és error contractot ellenőrzi. Backward/forward compatibility policy, version negotiation és breaking-change gate legyen explicit; a sample payload nem helyettesít contract assertiont.

## Források
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/en-us/sql/relational-databases/)
