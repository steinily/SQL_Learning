---
schema_version: 1
id: DBKB-MDM-0004
title: Golden Records
type: technology
primary_domain: master-data
secondary_domains: [data-quality]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0003]
related: []
aliases: [golden record]
search_keywords: [golden record, survivorship, source precedence, canonical entity]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Golden record purpose, source precedence, evidence and conflict handling are defined]
---
# Golden Records

Golden record canonical entity representation, amely source recordsból matching, survivorship, precedence és steward review alapján áll elő. Field-level provenance, confidence, conflict state, merge/unmerge path és correction audit nélkül a „golden” státusz nem visszakövethető.

## Források
- [ISO 8000](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
