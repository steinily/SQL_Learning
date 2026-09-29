---
schema_version: 1
id: DBKB-SEC-0025
title: Security Privacy Exercise
type: exercise
primary_domain: security-privacy
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0021, DBKB-SEC-0024]
related: []
aliases: [database security exercise]
search_keywords: [security exercise, access review, breach drill, evidence]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050, SRC-000052]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Security Privacy Exercise

Futtass tabletop exercise-t egy compromised service credential, túlzott database privilege és personal-data exposure esetére. Készíts threat modelt, containment döntést, access revocationt, evidence indexet, privacy/legal escalationt és recovery verificationt; execution-verified csak tényleges gyakorlat után használható.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
