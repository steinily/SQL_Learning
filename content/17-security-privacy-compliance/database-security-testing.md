---
schema_version: 1
id: DBKB-SEC-0023
title: Database Security Testing
type: playbook
primary_domain: security-privacy
secondary_domains: [testing]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0008, DBKB-SEC-0020]
related: []
aliases: [database security assessment]
search_keywords: [security test, privilege test, injection test, configuration assessment]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050, SRC-000051, SRC-000053]
acceptance_criteria: [Test scope, safe execution, findings and retest evidence are defined]
---
# Database Security Testing

Security testing-ben különítsd el a static configuration review-t, privilege/effective access testet, negative authorization testet, injection testet, vulnerability scan-t és penetration testet. Csak engedélyezett, isolated scope-ban futtasd, és minden findinghez reproduction, severity, remediation és retest evidence tartozzon.

## Források
- [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [PCI DSS](https://www.pcisecuritystandards.org/standards/pci-dss/)
