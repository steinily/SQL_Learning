---
schema_version: 1
id: DBKB-ORA-0008
title: Oracle Security
type: technology
primary_domain: oracle
secondary_domains: [security, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0007]
related: [DBKB-SEC-0001]
aliases: [Oracle access control]
search_keywords: [Oracle privilege, role, auditing, encryption, least privilege]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Identity, privilege, audit and encryption controls are mapped to risk]
---
# Oracle Security

Oracle security baseline: named identities, role-based least privilege, controlled ownership/schema boundaries, protected credentials, auditable administrative actions és encrypted transport/storage where required. A privilege grant legyen purpose- és expiry-controlled.

Review access paths, public grants, definer/invoker rights, audit retention és key-management ownership. Vendor feature availability and licensing is release-sensitive; security control evidence requires an actual configuration review.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
