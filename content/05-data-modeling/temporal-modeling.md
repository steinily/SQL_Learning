---
schema_version: 1
id: DBKB-MODL-0011
title: Temporal Modeling
type: concept
primary_domain: data-modeling
secondary_domains: [temporal-data, analytics]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0015, DBKB-MODL-0010]
related: [DBKB-ASQL-0020, DBKB-ASQL-0021]
aliases: [effective dating, bitemporal modeling]
search_keywords: [valid time, transaction time, effective_from, effective_to, history]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MODL-0002]
source_ids: [SRC-000013, SRC-000014]
acceptance_criteria: [Valid és transaction time-t elkülönít, Interval boundary és overlap policyt ad]
---
# Temporal Modeling

Valid time azt jelzi, mikor igaz egy domain tény; transaction/system time azt, mikor rögzítette a
database. Egy current table csak a jelen állapotot őrzi; history vagy bitemporal model audit és
„as-of” kérdésekhez szükséges.

Effective intervalnál válassz half-open contractot: `[valid_from, valid_to)`. Overlap prevention,
open-ended current row, timezone és correction/backdating policy legyen constrainttel vagy transaction
workflow-val védve. Calendar month és elapsed duration nem azonos.

As-of querynél minden kapcsolódó entity ugyanazon temporal cutot használja, különben impossible
hybrid state keletkezhet. Backfill és late-arriving correction külön migration/runbook.

## Források

- [PostgreSQL 18 — Date/Time Types](https://www.postgresql.org/docs/18/datatype-datetime.html)
- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
