---
schema_version: 1
id: DBKB-REC-0056
title: Change Incident Playbook
type: playbook
primary_domain: recipes
secondary_domains: [change-management, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0055]
related: [DBKB-MIG-0001]
aliases: [failed change runbook]
search_keywords: [failed deployment, rollback, canary, schema change, incident]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Change failure detection, abort, rollback, validation and communication are actionable]
---
# Change Incident Playbook

Change failurekor freeze further mutations, record version/config/contract and first bad signal, compare canary vs baseline, then choose abort, rollback or forward-fix ownerrel. Preserve data/schema/offset/backup evidence before cleanup.

Rollback után validate availability, correctness, compatibility, replication/lag, quality and consumer state. Post-incidentben update-eld ADR/change record, test gap, guardrail, runbook és approval evidence-et; „revert command succeeded” nem elég.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
