---
schema_version: 1
id: DBKB-SEC-0016
title: Compliance Control Mapping
type: playbook
primary_domain: security-privacy
secondary_domains: [compliance, governance]
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
aliases: [control crosswalk]
search_keywords: [control mapping, requirement, evidence, gap assessment]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050, SRC-000052, SRC-000053]
acceptance_criteria: [Requirement-to-control mapping and evidence ownership are specified]
---
# Compliance Control Mapping

Control mapping-ben requirement, applicability, control objective, implementation, owner, evidence source, frequency, exception és residual gap szerepeljen. Egy technical setting önmagában nem bizonyítja a control operating effectiveness-ét; sample, review és timestamp szükséges.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/)
