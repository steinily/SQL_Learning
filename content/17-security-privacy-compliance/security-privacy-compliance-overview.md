---
schema_version: 1
id: DBKB-SEC-0001
title: Security Privacy and Compliance Overview
type: overview
primary_domain: security-privacy
secondary_domains: [governance, compliance]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0001]
related: []
aliases: [database security overview]
search_keywords: [database security, privacy, compliance, controls]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050, SRC-000052]
acceptance_criteria: [Security privacy compliance scope and evidence are defined]
---
# Security Privacy and Compliance Overview

Database security az identity, authorization, data protection, secure query construction, audit és incident response rétegeit fogja össze. Privacy és compliance scope-ot a tényleges data processing, cardholder-data exposure, jurisdiction és control evidence alapján kell meghatározni.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
