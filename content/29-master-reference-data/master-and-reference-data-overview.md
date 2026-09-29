---
schema_version: 1
id: DBKB-MDM-0001
title: Master and Reference Data Overview
type: overview
primary_domain: master-data
secondary_domains: [governance, data-quality]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0001]
related: []
aliases: [MDM overview]
search_keywords: [master data, reference data, golden record, stewardship]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000083, SRC-000084, SRC-000085]
acceptance_criteria: [Master/reference distinction, governance and evidence are defined]
---
# Master and Reference Data Overview

Master data durable business entity-ket, reference data pedig controlled code/value seteket kezel, amelyek több systemben közös jelentést igényelnek. Governance, identity, matching, survivorship, quality, lifecycle és steward approval nélkül nincs reliable shared record.

## Források
- [W3C SKOS](https://www.w3.org/TR/skos-reference/)
- [ISO 8000](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
