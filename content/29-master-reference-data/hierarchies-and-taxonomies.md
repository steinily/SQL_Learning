---
schema_version: 1
id: DBKB-MDM-0006
title: Hierarchies and Taxonomies
type: technology
primary_domain: master-data
secondary_domains: [metadata, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openmetadata]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MDM-0005]
related: [DBKB-MDM-0003]
aliases: [classification hierarchy, taxonomy]
search_keywords: [hierarchy, taxonomy, broader, narrower, parent child]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MDM-0001]
source_ids: [SRC-000083, SRC-000085]
acceptance_criteria: [Taxonomy and hierarchy semantics, ownership and cycle prevention are explained]
---
# Hierarchies and Taxonomies

A taxonomy controlled classification, a hierarchy pedig parent-child relationship. A domain should define whether a node may have one parent, multiple parents, or no parent, and whether relationships are temporal. SKOS `broader`/`narrower` relations are useful vocabulary semantics; they do not by themselves enforce database constraints.

Cycle prevention, stable identifiers, effective dates and steward approval are required before a hierarchy is consumed for reporting or access rules. Validate imports with a graph check and reject orphan or cyclic nodes.

## Források
- [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)
- [OpenMetadata Documentation](https://docs.open-metadata.org/)
