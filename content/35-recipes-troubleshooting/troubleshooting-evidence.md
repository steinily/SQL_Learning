---
schema_version: 1
id: DBKB-REC-0040
title: Troubleshooting Evidence
type: reference
primary_domain: recipes
secondary_domains: [audit, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0039]
related: [DBKB-OPS-0001]
aliases: [incident evidence checklist]
search_keywords: [evidence, incident timeline, query ID, checksum, audit trail]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000080]
acceptance_criteria: [A reusable evidence checklist preserves reproducibility and auditability]
---
# Troubleshooting Evidence

Evidence checklist: UTC timeline; incident/severity/owner; affected resource/tenant; deployment/config/contract revision; metrics/logs/traces; query/run/offset/LSN IDs; sample input/output; schema/quality/lineage; commands and tool versions; decision/approval; rollback/recovery; post-check and retention.

Sensitive payloadot redaction/tokenization mellett őrizz; evidence hash vagy immutable storage segíti a tamper detectiont. „Observed”, „inferred” és „executed” állítást külön címkézd.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
