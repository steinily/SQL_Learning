---
schema_version: 1
id: DBKB-INT-0019
title: Checksum and Corruption
type: troubleshooting
primary_domain: database-internals
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0003, DBKB-INT-0017]
related: [DBKB-INT-0024]
aliases: [page checksum, data corruption]
search_keywords: [data corruption, page checksum, checksum verification]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Checksum detection és incident evidence folyamatot ad destructive claim nélkül]
---
# Checksum and Corruption

Page checksum segíthet észlelni bizonyos storage corruption eseményeket, de nem bizonyítja az adat teljes szemantikai helyességét. Gyanú esetén izoláld a bizonyítékot, ellenőrizd backup/replica példányt és kövesd az incident runbookot.

## Források
- [PostgreSQL 18 — Data Checksums](https://www.postgresql.org/docs/18/checksum.html)
