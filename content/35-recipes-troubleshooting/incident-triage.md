---
schema_version: 1
id: DBKB-REC-0039
title: Incident Triage
type: troubleshooting
primary_domain: recipes
secondary_domains: [operations, reliability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0038]
related: [DBKB-OPS-0001]
aliases: [data incident triage]
search_keywords: [incident triage, severity, blast radius, containment, evidence]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [Severity, scope, evidence, containment, communication and handoff are actionable]
---
# Incident Triage

Első öt perc: classify availability/data correctness/security/cost impact, identify affected tenant/dataset/consumer, freeze risky changes és assign incident commander/technical owner. Preserve timestamped metrics, logs, query/run IDs, schema/contract and recent change list.

Set severity and update cadence; containment legyen reversible. Handoffnál documentáld hypothesis, confirmed evidence, next check, rollback decision és customer/business communication. Root cause csak validated evidence után.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
