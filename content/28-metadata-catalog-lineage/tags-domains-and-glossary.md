---
schema_version: 1
id: DBKB-META-0006
title: Tags Domains and Glossary
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
prerequisites: [DBKB-META-0005]
related: []
aliases: [catalog taxonomy]
search_keywords: [tag, domain, glossary term, classification, taxonomy]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000082]
acceptance_criteria: [Tag/domain/glossary semantics, ownership and lifecycle are defined]
---
# Tags Domains and Glossary

Tags classificationt, domains organizational/context ownershipet, glossary terms business meaninget adnak. Controlled vocabulary, hierarchy, synonym/deprecation policy, owner és review date kell; free-text tag proliferation csökkenti search és governance quality-t.

## Források
- [DataHub Documentation](https://docs.datahub.com/)
