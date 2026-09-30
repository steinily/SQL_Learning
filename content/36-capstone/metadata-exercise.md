---
schema_version: 1
id: DBKB-CAP-0036
title: Metadata Exercise
type: exercise
primary_domain: capstone
secondary_domains: [metadata, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata, openlineage]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0035]
related: [DBKB-META-0001]
aliases: [metadata lab]
search_keywords: [metadata exercise, catalog, lineage, ownership, freshness]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000080, SRC-000085]
acceptance_criteria: [Learner registers assets, ownership, lineage, quality and impact evidence]
---
# Metadata Exercise

Regisztrálj egy datasetet catalogba stable identityvel, owner/stewarddal, domain/classificationnel, quality/Freshness SLO-val és OpenLineage job/run/dataset eventtel.

Mutass broken lineage, stale metadata és ownership change esetet; készíts impact analysis-t és post-fix verificationt. Evidence: API output, last-seen timestamps, lineage graph és access audit.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
