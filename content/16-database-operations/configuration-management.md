---
schema_version: 1
id: DBKB-OPS-0004
title: Configuration Management
type: playbook
primary_domain: database-operations
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0003]
related: []
aliases: [database configuration]
search_keywords: [configuration drift, parameters, baseline]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Configuration baseline, change and drift evidence are defined]
---
# Configuration Management

Configuration baseline-ben legyenek a parameter values, authentication, logging, resource limits és storage paths. Változtatás előtt capture-eld az effective configuration-t, alkalmazd kontrolláltan, majd hasonlítsd össze a post-change állapottal; a default érték nem tekinthető univerzálisnak.

## Források
- [PostgreSQL — Server Configuration](https://www.postgresql.org/docs/current/runtime-config.html)
