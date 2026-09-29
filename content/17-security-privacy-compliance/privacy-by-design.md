---
schema_version: 1
id: DBKB-SEC-0011
title: Privacy by Design
type: concept
primary_domain: security-privacy
secondary_domains: [privacy]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0001]
related: []
aliases: [data protection by design]
search_keywords: [privacy by design, data minimization, purpose limitation]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000052]
acceptance_criteria: [Privacy design principles are translated to database decisions]
---
# Privacy by Design

Privacy by design a schema, collection, retention, access és observability döntéseibe korán beépíti a data minimization, purpose limitation, accuracy, confidentiality és accountability szempontokat. A döntéseket processing purpose, risk assessment és review evidence mellett dokumentáld.

## Források
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
