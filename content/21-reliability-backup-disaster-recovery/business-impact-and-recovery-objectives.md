---
schema_version: 1
id: DBKB-DR-0002
title: Business Impact and Recovery Objectives
type: concept
primary_domain: reliability
secondary_domains: [governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0001]
related: []
aliases: [BIA RPO RTO]
search_keywords: [business impact analysis, RPO, RTO, criticality, recovery tier]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000064]
acceptance_criteria: [Business impact, RPO/RTO and recovery tier decisions are explained]
---
# Business Impact and Recovery Objectives

Business impact analysis kapcsolja a service criticality-t, maximum tolerable downtime-ot, data loss tolerance-t, dependency-t és recovery tier-t. RPO/RTO legyen measurable target; ha a test actual resultja eltér, remediation vagy objective renegotiation szükséges.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
