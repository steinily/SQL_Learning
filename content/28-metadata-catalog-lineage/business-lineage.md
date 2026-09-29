---
schema_version: 1
id: DBKB-META-0008
title: Business Lineage
type: concept
primary_domain: lineage
secondary_domains: [governance, analytics]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openlineage, datahub]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0007]
related: []
aliases: [business data lineage]
search_keywords: [business lineage, KPI, report, process, impact analysis]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000081, SRC-000082]
acceptance_criteria: [Business process, metric, report and technical lineage linking are defined]
---
# Business Lineage

Business lineage technical datasets-et business processhez, KPI-hoz, reporthoz, policyhoz és decision contexthez kapcsolja. Mappinget steward review-val tartsd fenn; technical graph automatikus presence-e nem bizonyítja a business interpretation helyességét.

## Források
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [DataHub Documentation](https://docs.datahub.com/)
