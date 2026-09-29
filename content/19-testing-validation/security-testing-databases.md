---
schema_version: 1
id: DBKB-TEST-0014
title: Security Testing Databases
type: playbook
primary_domain: testing-validation
secondary_domains: [security-privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0013]
related: []
aliases: [database security test plan]
search_keywords: [security testing, privilege escalation, injection, hardening]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000057, SRC-000059]
acceptance_criteria: [Authorization, injection, configuration and evidence controls are covered]
---
# Security Testing Databases

Database security testing scope-ja legyen authorization, privilege escalation, SQL injection, secret exposure, TLS/configuration, audit completeness és vulnerability coverage. Írásos authorization, safe payload, data masking, finding severity és retest evidence nélkül a security test nem tekinthető validnak.

## Források
- [NIST SP 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final)
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/en-us/sql/relational-databases/)
