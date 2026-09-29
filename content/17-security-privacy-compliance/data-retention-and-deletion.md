---
schema_version: 1
id: DBKB-SEC-0013
title: Data Retention and Deletion
type: playbook
primary_domain: security-privacy
secondary_domains: [privacy, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0012]
related: []
aliases: [retention and erasure]
search_keywords: [retention, deletion, erasure, legal hold]
risk: destructive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000052]
acceptance_criteria: [Retention schedule, legal hold and deletion evidence are covered]
---
# Data Retention and Deletion

Retention schedule a purpose, legal requirement, backup behavior, legal hold és deletion trigger alapján álljon össze. Deletion runbooknak kezelnie kell cascade, replicas, caches, exports és backup expiry kérdéseit, valamint bizonyítania kell a scope-ot és a completed verification-t.

## Források
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
