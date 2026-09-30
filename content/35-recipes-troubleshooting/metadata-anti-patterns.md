---
schema_version: 1
id: DBKB-REC-0047
title: Metadata Anti-Patterns
type: error
primary_domain: recipes
secondary_domains: [metadata, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0046]
related: [DBKB-META-0001]
aliases: [catalog mistakes]
search_keywords: [metadata anti-pattern, stale lineage, orphan asset, missing owner, catalog theater]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000080, SRC-000085]
acceptance_criteria: [Metadata anti-pattern detection and remediation are concrete]
---
# Metadata Anti-Patterns

Anti-pattern a catalog lineage nélkül, stale/unowned asset, duplicate identifier, glossary fogalom definition nélkül, quality tag evidence nélkül és metadata sync csak success response alapján.

Detectáld last-seen/freshness, owner coverage, broken lineage, duplicate asset és consumer feedback alapján. Remediation: stable identity, steward assignment, source integration, freshness SLO, review/retirement és audit evidence.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
