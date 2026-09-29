---
schema_version: 1
id: DBKB-META-0002
title: Technical Metadata
type: concept
primary_domain: metadata
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openlineage, datahub]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0001]
related: []
aliases: [technical metadata]
search_keywords: [schema metadata, column, type, partition, statistics, owner]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000082]
acceptance_criteria: [Technical metadata fields, identity, freshness and source are explained]
---
# Technical Metadata

Technical metadata table/column/schema identityt, typeot, constraintot, partitiont, statistics-t, locationt, versiont és operational state-et ír le. Capture source, timestamp, environment és freshness is kell; extracted schema snapshot nem feltétlenül effective runtime state.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [DataHub Documentation](https://docs.datahub.com/)
