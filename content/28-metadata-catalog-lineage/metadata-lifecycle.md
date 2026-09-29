---
schema_version: 1
id: DBKB-META-0012
title: Metadata Lifecycle
type: playbook
primary_domain: metadata
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [datahub, openlineage]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0011]
related: []
aliases: [metadata retention lifecycle]
search_keywords: [metadata onboarding, update, deprecation, archive, deletion]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000082]
acceptance_criteria: [Onboard, update, deprecate, archive, delete and review states are defined]
---
# Metadata Lifecycle

Metadata lifecycle onboarding → enrichment → review → active → deprecated → archived/deleted stateeket kezel. Source asset deletion, ownership change, schema version, lineage expiry, glossary term deprecation és retention policy legyen idempotent és auditable; stale catalog recordet ne rejts el silent delete-tel.

## Források
- [DataHub Documentation](https://docs.datahub.com/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
