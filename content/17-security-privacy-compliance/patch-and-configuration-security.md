---
schema_version: 1
id: DBKB-SEC-0020
title: Patch and Configuration Security
type: playbook
primary_domain: security-privacy
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0019]
related: []
aliases: [secure database baseline]
search_keywords: [hardening, patch baseline, configuration drift, secure defaults]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050]
acceptance_criteria: [Secure baseline, drift detection and patch evidence are described]
---
# Patch and Configuration Security

Secure baseline-ben legyen supported version, disabled unused features, network exposure, authentication, logging, encryption és privilege settings. Drift detection, patch test, maintenance window, rollback és post-change verification együtt ad operational evidence-et.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
