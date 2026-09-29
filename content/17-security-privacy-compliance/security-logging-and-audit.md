---
schema_version: 1
id: DBKB-SEC-0015
title: Security Logging and Audit
type: technology
primary_domain: security-privacy
secondary_domains: [observability, compliance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0004]
related: []
aliases: [database audit logging]
search_keywords: [audit log, security events, tamper resistance, review]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050, SRC-000053]
acceptance_criteria: [Security event coverage, protection, retention and review are defined]
---
# Security Logging and Audit

Audit log policy-ben legyen authentication, privilege, schema, data access, configuration és administrative event coverage, actor identity, timestamp consistency, retention és alerting. A log integrity, access restriction és review evidence ugyanolyan fontos, mint maga az event capture.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/)
