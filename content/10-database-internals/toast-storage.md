---
schema_version: 1
id: DBKB-INT-0014
title: TOAST Storage
type: technology
primary_domain: database-internals
secondary_domains: [storage]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0003]
related: [DBKB-INT-0020]
aliases: [large attribute storage]
search_keywords: [TOAST, oversized attribute, out-of-line storage]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [TOAST out-of-line/compression behaviorét és query impactot írja le]
---
# TOAST Storage

TOAST oversized attributeokat tömörít vagy külön TOAST relationben tárol, hogy a main heap tuple page-kompatibilis maradjon. Large value access extra I/O-t és storage behavior-t okozhat; schema/query tuningnál mérd.

## Források
- [PostgreSQL 18 — TOAST](https://www.postgresql.org/docs/18/storage-toast.html)
