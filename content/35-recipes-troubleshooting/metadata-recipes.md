---
schema_version: 1
id: DBKB-REC-0016
title: Metadata Recipes
type: playbook
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
prerequisites: [DBKB-REC-0015]
related: [DBKB-META-0001]
aliases: [catalog recipe]
search_keywords: [metadata, catalog, ownership, lineage, glossary]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000080, SRC-000085]
acceptance_criteria: [Catalog registration, ownership, lineage freshness and metadata evidence are covered]
---
# Metadata Recipes

Catalog registration recipeben stable dataset/service identityt, owner/stewardot, domain, classificationt, glossary és source/lineage reference-et adj. Ingest után verify-old a metadata completeness, last-seen timestampot és ownership validityt.

Lineage vagy tag update ne legyen „successful” pusztán API response alapján: ellenőrizd a target catalog queryt és downstream impactot. Sensitive metadata redaction, access control, retention és rollback legyen dokumentált.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
