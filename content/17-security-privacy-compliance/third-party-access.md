---
schema_version: 1
id: DBKB-SEC-0022
title: Third Party Access
type: technology
primary_domain: security-privacy
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0005]
related: []
aliases: [vendor database access]
search_keywords: [third party, vendor access, just in time, support account]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050, SRC-000052]
acceptance_criteria: [Vendor access scope, approval, monitoring and revocation are covered]
---
# Third Party Access

Third-party access legyen time-bound, purpose-bound, least privilege és approvalhoz kötött. Preferáld a monitored, just-in-time access-t; session, query és data export evidence legyen megőrizhető, majd a contract vagy support window végén revoke-old a hozzáférést.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
