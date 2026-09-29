---
schema_version: 1
id: DBKB-SEC-0005
title: Least Privilege
type: concept
primary_domain: security-privacy
secondary_domains: [identity]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0004]
related: []
aliases: [minimum necessary access]
search_keywords: [least privilege, privilege minimization, access review]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050]
acceptance_criteria: [Least privilege design and periodic review are stated]
---
# Least Privilege

Least privilege a taskhez szükséges minimális access scope, időtartam és execution context megadását jelenti. Tervezd külön a read, write, DDL, administration és support privileges-t, mérd a tényleges használatot, majd review-val csökkentsd a felesleges jogosultságokat.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
