---
schema_version: 1
id: DBKB-MODL-0016
title: Data Modeling Anti-Patterns
type: troubleshooting
primary_domain: data-modeling
secondary_domains: [data-quality, operations]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0005, DBKB-MODL-0015]
related: [DBKB-MODL-0006, DBKB-MODL-0023]
aliases: [schema anti-pattern]
search_keywords: [anti-pattern, comma list, EAV, generic table, missing constraint]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria: [Legalább hat anti-pattern tünetét és javítási irányát megadja, Constraint és grain hiányát kiemeli]
---
# Data Modeling Anti-Patterns

Gyakori anti-pattern a comma-separated ID list, amely elveszíti FK és cardinality enforcementet;
az „one giant table”, amely több grain-t kever; az EAV ellenőrzés nélkül; `SELECT *`-ra épülő interface;
és a surrogate key business uniqueness nélkül.

További jel a nullable mindenre, implicit timezone, audit history nélküli overwrite, tenant filter
application conventionként, valamint denormalized cache refresh policy nélkül. A tünet önmagában nem
bizonyít hibát; domain, workload és contract alapján diagnosztizálj.

Remediation: rögzíts grain-t, business identityt és invariánst; add hozzá a megfelelő constraintet;
válaszd szét a lifecycle-okat; majd mérj representative workloadot.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
