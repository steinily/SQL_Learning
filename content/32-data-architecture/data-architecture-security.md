---
schema_version: 1
id: DBKB-DARCH-0011
title: Data Architecture Security
type: technology
primary_domain: data-architecture
secondary_domains: [security, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [togaf, dcat]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0010]
related: [DBKB-SEC-0001]
aliases: [architecture security]
search_keywords: [data architecture security, classification, trust boundary, least privilege]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Classification, trust boundaries, identity, encryption and security review are covered]
---
# Data Architecture Security

Security architecture kezdőpontja a data classification, threat boundary és identity flow. Jelöld a sensitive/regulated data-t, producer-consumer trust boundary-t, encryption in transit/at rest-et, key ownershipot és least-privilege access pathot.

Architecture reviewben ellenőrizd a tenant isolationt, exfiltration path-okat, backup/snapshot exposure-t, catalog metadata sensitivity-t és incident evidence-et. A federated domain governance security baseline-ja legyen kötelező, exception expiry-vel.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
