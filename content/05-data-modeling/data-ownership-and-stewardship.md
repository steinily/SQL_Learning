---
schema_version: 1
id: DBKB-MODL-0022
title: Data Ownership and Stewardship
type: concept
primary_domain: data-modeling
secondary_domains: [data-governance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0001, DBKB-MODL-0009]
related: [DBKB-MODL-0023, DBKB-MODL-0024]
aliases: [data steward]
search_keywords: [ownership, steward, source of truth, SLA, lifecycle]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-MODL-0003]
source_ids: [SRC-000016]
acceptance_criteria: [Owner, steward és operator szerepet elkülönít, Lifecycle és quality responsibilityt rögzít]
---
# Data Ownership and Stewardship

Owner dönt a jelentésről, policy-ról és prioritásról; steward a definition, quality rule és metadata
operationalizálását végzi; operator futtatja és monitorozza a platformot. Egy személy több szerepet
viselhet, de a felelősség ne legyen implicit.

Minden kritikus entityhez legyen source of truth, quality SLA/SLO, change approval, retention,
incident contact és downstream impact owner. A foreign key technikai integrityt véd, nem rendezi az
organizational ownershipet.

## Források

- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
