---
schema_version: 1
id: DBKB-SEC-0014
title: Data Subject Rights Operations
type: playbook
primary_domain: security-privacy
secondary_domains: [privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0013]
related: []
aliases: [DSAR operations]
search_keywords: [data subject request, access request, rectification, erasure]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000052]
acceptance_criteria: [Rights request intake, identity verification, search and response evidence are defined]
---
# Data Subject Rights Operations

Data subject request workflow-ban legyen intake, identity verification, scope discovery, exception/legal hold review, export vagy rectification, deletion és response evidence. A cross-system search coverage-t és az unresolved data source-okat explicit módon jelezd; jogi határidőt ne helyettesíts technikai feltételezéssel.

## Források
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
