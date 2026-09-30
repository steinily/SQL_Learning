---
schema_version: 1
id: DBKB-REC-0045
title: Data Quality Anti-Patterns
type: error
primary_domain: recipes
secondary_domains: [data-quality, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, openmetadata]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-REC-0044]
related: [DBKB-DQ-0001]
aliases: [quality mistakes]
search_keywords: [quality theater, hidden null, silent threshold, no owner, duplicate rule]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000085]
acceptance_criteria: [Quality anti-patterns include measurable detection and remediation]
---
# Data Quality Anti-Patterns

Anti-pattern a rule owner/threshold nélkül, sample-only validation, silent threshold relaxation, rejected record discard, duplicate rule, quality score business semantics nélkül és breach consumer communication nélkül.

Detectionhez rule registry, trend, failed sample, quarantine count és owner SLA kell. Remediation: explicit severity/owner, source evidence, correction/replay, downstream reconciliation és reviewed threshold change.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
