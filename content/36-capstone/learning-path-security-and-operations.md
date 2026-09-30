---
schema_version: 1
id: DBKB-CAP-0080
title: Learning Path Security and Operations
type: learning-path
primary_domain: capstone
secondary_domains: [security, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0079]
related: [DBKB-CAP-0037, DBKB-CAP-0056]
aliases: [security operations path]
search_keywords: [security learning path, IAM, audit, SLO, backup, incident]
risk: security-sensitive
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Ordered security/operations path with identity, monitoring, recovery and incident milestones]
---
# Learning Path Security and Operations

Sorrend: classification/trust boundary → IAM/least privilege → TLS/key/audit → SLO/observability → backup/restore → incident/change playbook → security/recovery exercises/cases.

Exit criteria: positive/negative access evidence, alert/runbook, restore/failover drill, incident timeline, rollback és post-incident remediation.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
