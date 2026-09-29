---
schema_version: 1
id: DBKB-TEST-0017
title: Test Data Management
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
prerequisites: [DBKB-TEST-0016]
related: []
aliases: [test data lifecycle]
search_keywords: [test data, masking, synthetic data, retention, refresh]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000057]
acceptance_criteria: [Synthetic/masked data, access, retention and cleanup are covered]
---
# Test Data Management

Test data lehet synthetic, masked vagy minimalized production-derived; choice-ot sensitivity, representativeness és legal policy alapján indokold. Access, refresh, retention, lineage, seed reproducibility és cleanup legyen auditálható, és production personal data ne kerüljön kontroll nélkül tesztkörnyezetbe.

## Források
- [NIST SP 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final)
