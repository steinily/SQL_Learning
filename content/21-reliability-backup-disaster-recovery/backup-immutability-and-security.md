---
schema_version: 1
id: DBKB-DR-0008
title: Backup Immutability and Security
type: technology
primary_domain: backup
secondary_domains: [security-privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0003]
related: []
aliases: [immutable backup]
search_keywords: [immutability, backup encryption, ransomware, access control]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000063, SRC-000064, SRC-000065]
acceptance_criteria: [Backup access, encryption, immutability and restore key availability are covered]
---
# Backup Immutability and Security

Backup securityhez encryption, least privilege, separate admin boundary, immutable/append-only retention, deletion protection, key lifecycle és restore access kell. Immutability csak akkor hasznos, ha a recovery identity és key material elérhető, valamint a restore path rendszeresen tesztelt.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
