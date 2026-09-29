---
schema_version: 1
id: DBKB-MDM-0012
title: Master Data Security
type: technology
primary_domain: master-data
secondary_domains: [security, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0011]
related: [DBKB-SEC-0001]
aliases: [MDM access control]
search_keywords: [master data security, least privilege, masking, audit]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Least privilege, sensitive attributes, audit and retention controls are covered]
---
# Master Data Security

Apply least privilege by domain, attribute és operation; separate read, propose, approve, publish és administer permissions. Sensitive attributes legyenek masked vagy tokenized a non-production környezetben, és export paths legyenek kontrolláltak.

Auditáld a record access-t, bulk exportot, survivorship override-ot és reference value változásokat. Retention, deletion és legal hold policy-ket a data owner és privacy/security function hagyja jóvá; a catalog ownership önmagában nem authorization.

## Források
- [ISO 8000 Data Quality](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
