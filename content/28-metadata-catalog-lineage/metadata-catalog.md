---
schema_version: 1
id: DBKB-META-0004
title: Metadata Catalog
type: technology
primary_domain: metadata
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [datahub]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-META-0003]
related: []
aliases: [data catalog]
search_keywords: [catalog ingestion, search, ownership, tags, domains, glossary]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000082]
acceptance_criteria: [Catalog entities, ingestion, search, ownership and governance are scoped]
---
# Metadata Catalog

Catalog ingestion source connectorsból entities, schema, tags, owners, domains, quality és lineage metadata-t gyűjt. Ingestion schedule, conflict resolution, deletion/deprecation, access, freshness és failed extractor monitoring szükséges; UI search coverage nem bizonyít catalog completeness-t.

## Források
- [DataHub Documentation](https://docs.datahub.com/)
