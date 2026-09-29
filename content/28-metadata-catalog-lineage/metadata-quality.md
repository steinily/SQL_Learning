---
schema_version: 1
id: DBKB-META-0010
title: Metadata Quality
type: playbook
primary_domain: metadata
secondary_domains: [data-quality]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openlineage, datahub]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0009]
related: []
aliases: [metadata quality]
search_keywords: [metadata completeness, freshness, lineage coverage, catalog drift]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000082]
acceptance_criteria: [Metadata completeness, freshness, correctness and coverage controls are defined]
---
# Metadata Quality

Metadata quality mérje entity coverage, owner/tag completeness, schema freshness, lineage edge coverage, glossary definition, source consistency és stale/deleted asset handling értékeket. Catalog record PASS nem jelenti lineage accuracy-t; sampled verification és steward acknowledgement szükséges.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [DataHub Documentation](https://docs.datahub.com/)
