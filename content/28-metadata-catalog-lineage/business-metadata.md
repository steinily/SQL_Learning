---
schema_version: 1
id: DBKB-META-0003
title: Business Metadata
type: concept
primary_domain: metadata
secondary_domains: [governance, analytics]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [datahub]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0002]
related: []
aliases: [business metadata]
search_keywords: [business definition, KPI, glossary, owner, classification]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000081, SRC-000082]
acceptance_criteria: [Business definition, metric, owner and classification are covered]
---
# Business Metadata

Business metadata glossary termet, metric definitiont, business purpose-t, classificationt, owner/stewardot és consumer contextet ad. Definition legyen versioned és review date-del rendelkező; technical field name vagy dashboard label önmagában nem business meaning.

## Források
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [DataHub Documentation](https://docs.datahub.com/)
