---
schema_version: 1
id: DBKB-SEC-0017
title: PCI DSS Database Controls
type: technology
primary_domain: security-privacy
secondary_domains: [compliance]
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
aliases: [cardholder data database controls]
search_keywords: [PCI DSS, cardholder data, payment account data, segmentation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000053]
acceptance_criteria: [PCI scope, access, logging and testing concerns are scoped]
---
# PCI DSS Database Controls

PCI DSS database controlok csak cardholder data environment scope után értelmezhetők. Inventory, segmentation, least privilege, authentication, encryption, vulnerability management, logging és testing evidence legyen traceable a követelményhez és assessor review-hoz.

## Források
- [PCI Security Standards Council — PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/)
