---
schema_version: 1
id: DBKB-SEC-0018
title: GDPR Database Controls
type: technology
primary_domain: security-privacy
secondary_domains: [compliance, privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0016]
related: []
aliases: [GDPR data controls]
search_keywords: [GDPR, personal data, controller, processor, DPIA]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000052]
acceptance_criteria: [GDPR-relevant database controls and legal caveat are stated]
---
# GDPR Database Controls

GDPR database controls a processing purpose, lawful basis, data minimization, access, retention, subject rights, breach response és processor chain köré szerveződnek. A technical implementationt privacy/legal review-hoz kell kötni; ez a dokumentum nem jogi tanácsadás.

## Források
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
