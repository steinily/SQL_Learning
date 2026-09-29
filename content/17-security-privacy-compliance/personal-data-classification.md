---
schema_version: 1
id: DBKB-SEC-0012
title: Personal Data Classification
type: reference
primary_domain: security-privacy
secondary_domains: [privacy, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0011]
related: []
aliases: [data classification]
search_keywords: [personal data, sensitive data, classification, inventory]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000052]
acceptance_criteria: [Classification criteria, ownership and inventory evidence are defined]
---
# Personal Data Classification

Classification inventory-ben legyen data element, purpose, subject, sensitivity, lawful processing context, owner, location, retention és downstream sharing. A column name alapján végzett automatikus besorolás csak candidate; domain review és evidence szükséges a végleges labelhez.

## Források
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
