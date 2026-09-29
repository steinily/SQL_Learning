---
schema_version: 1
id: DBKB-OPS-0014
title: Change Management
type: playbook
primary_domain: database-operations
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0013]
related: []
aliases: [database change control]
search_keywords: [change request, approval, maintenance window, rollback]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Change record, approval, execution and review are specified]
---
# Change Management

Database change record-ben szerepeljen business reason, affected objects, risk, dependencies, test evidence, approver, window, rollback és success criteria. Emergency change után is kell utólagos review és evidence; approval nem helyettesíti a technical validation-t.

## Források
- [PostgreSQL — Server Administration](https://www.postgresql.org/docs/current/admin.html)
