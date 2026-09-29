---
schema_version: 1
id: DBKB-MODL-0009
title: Lookup and Reference Data
type: concept
primary_domain: data-modeling
secondary_domains: [data-governance, data-quality]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0004, DBKB-SQL-0022]
related: [DBKB-MODL-0014, DBKB-MODL-0022]
aliases: [code table, reference table]
search_keywords: [lookup, reference data, code, effective date, foreign key]
risk: safe
version_sensitive: false
review_cycle: 12m
research_packages: [RP-MODL-0002]
source_ids: [SRC-000009, SRC-000013]
acceptance_criteria: [Reference row lifecycle-t és ownershipet megad, FK és active/effective állapotot különít el]
---
# Lookup and Reference Data

Lookup/reference table controlled vocabularyt vagy domain code-ot tárol: például country, status vagy
currency. A foreign key biztosítja, hogy fact table ne tároljon ismeretlen code-ot, de a reference
row lifecycle-ja külön policy.

Ne törölj aktívan hivatkozott code-ot vakon. `is_active`, effective interval vagy immutable code
segíthet, de a historical fact jelentése megmaradjon. A display label változhat; a stable code és
locale-specific label különválasztása gyakran helyes.

Ownership, approval, source authority, version és deprecation process legyen rögzítve. Hard-coded
application list és database lookup külön consistency risket hordoz.

A fixture-ekben a reference table FK-ja és invalid code rejectionje executable contract.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [PostgreSQL 18 — Date/Time Types](https://www.postgresql.org/docs/18/datatype-datetime.html)
