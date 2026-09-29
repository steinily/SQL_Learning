---
schema_version: 1
id: DBKB-DARCH-0004
title: Data Lifecycle Architecture
type: technology
primary_domain: data-architecture
secondary_domains: [governance, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [dcat, togaf]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0003]
related: [DBKB-STOR-0001, DBKB-META-0012]
aliases: [data lifecycle]
search_keywords: [data lifecycle, ingest, active, archive, retention, deletion]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093]
acceptance_criteria: [Ingest, active use, archive, retention and disposal states with controls are described]
---
# Data Lifecycle Architecture

Lifecycle state-ek: planned → ingested → validated → active → archived → expired/deleted. Minden transitionhöz owner, trigger, retention, legal hold, quality/security control és evidence tartozzon.

Catalogban a dataset/distribution/service identity maradjon stabil, miközben a physical storage vagy format változhat. Deletion legyen policy-driven és verifiable; replication, backup és downstream cache ne tartsa életben észrevétlenül a lejárt data-t.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
