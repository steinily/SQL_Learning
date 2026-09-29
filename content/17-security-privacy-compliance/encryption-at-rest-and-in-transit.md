---
schema_version: 1
id: DBKB-SEC-0007
title: Encryption at Rest and in Transit
type: technology
primary_domain: security-privacy
secondary_domains: [cryptography]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0006]
related: []
aliases: [database encryption]
search_keywords: [TLS, TDE, encryption at rest, key management]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000050]
acceptance_criteria: [Encryption layers, keys and verification are distinguished]
---
# Encryption at Rest and in Transit

Encryption in transit a client-server channel confidentiality/integrity-jét, encryption at rest pedig storage media és backup protection-jét célozza. Dokumentáld a TLS policy-t, cipher és certificate lifecycle-t, TDE vagy column-level encryption scope-ot, key ownership-et és restore során szükséges key availability-t.

## Források
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
