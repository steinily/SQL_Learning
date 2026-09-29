---
schema_version: 1
id: DBKB-SEC-0021
title: Security Incident Response
type: playbook
primary_domain: security-privacy
secondary_domains: [incident-management]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0015]
related: []
aliases: [database security incident]
search_keywords: [breach response, containment, forensics, notification]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050, SRC-000052]
acceptance_criteria: [Containment, evidence, notification and recovery responsibilities are separated]
---
# Security Incident Response

Security incident során preserve evidence-et, containd a credential vagy network exposure-t, és külön kezeld a technical recovery-t, privacy assessment-et, legal notification-t és stakeholder communication-t. A breach determination és határidő jogi/privacy döntés, nem pusztán database alert.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
