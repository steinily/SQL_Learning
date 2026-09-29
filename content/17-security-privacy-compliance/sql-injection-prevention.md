---
schema_version: 1
id: DBKB-SEC-0008
title: SQL Injection Prevention
type: technology
primary_domain: security-privacy
secondary_domains: [application-security]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0005]
related: []
aliases: [SQLi prevention]
search_keywords: [SQL injection, parameterized query, allow-list validation]
risk: security-sensitive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000051]
acceptance_criteria: [Parameterized queries, validation and privilege controls are explained]
---
# SQL Injection Prevention

SQL injection ellen a primary control a parameterized query vagy safe API; dynamic identifier vagy sort direction esetén explicit allow-list validation szükséges. Stored procedure önmagában nem garancia, ha string concatenation-t használ, és a database principal legyen least privilege.

## Források
- [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
