---
schema_version: 1
id: DBKB-CAP-0055
title: Reference Operations
type: reference
primary_domain: capstone
secondary_domains: [operations, reliability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0054]
related: [DBKB-OPS-0001]
aliases: [operations checklist]
search_keywords: [operations reference, SLO, backup, alert, runbook, change]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Operational readiness, monitoring, backup, change and incident checklist is provided]
---
# Reference Operations

Readiness: owner/on-call; SLO/error budget; capacity/quota; backup/restore evidence; replication/lag; alert/runbook; security/audit; change/canary/rollback; incident severity/communication; reconciliation; post-incident actions.

„Managed” vagy green dashboard nem helyettesíti a restore drillt és business validationt. Minden production actionhez scope, approval, evidence és reversibility tartozzon.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
