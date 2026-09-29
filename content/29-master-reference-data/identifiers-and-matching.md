---
schema_version: 1
id: DBKB-MDM-0005
title: Identifiers and Matching
type: technology
primary_domain: master-data
secondary_domains: [data-quality]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0004]
related: []
aliases: [entity matching]
search_keywords: [identifier, natural key, matching, deduplication, fuzzy match]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000084, SRC-000085]
acceptance_criteria: [Identifier, deterministic/fuzzy matching and confidence review are covered]
---
# Identifiers and Matching

Identifier lehet source/natural, enterprise surrogate vagy external identifier; mapping és collision policy kell. Matching deterministic keys, normalized attributes vagy fuzzy evidence alapján candidate-et adhat, de threshold, false match/negative review, merge approval és provenance nélkül automatikus merge veszélyes.

## Források
- [ISO 8000](https://www.iso.org/standard/50798.html)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
