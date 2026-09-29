---
schema_version: 1
id: DBKB-DQ-0007
title: Accuracy and Validity
type: concept
primary_domain: data-quality
secondary_domains: [data-modeling]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0006]
related: []
aliases: [data accuracy validity]
search_keywords: [accuracy, validity, domain rule, reference data, plausibility]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000079]
acceptance_criteria: [Accuracy versus validity and evidence limitations are explained]
---
# Accuracy and Validity

Validity azt méri, hogy az érték format/domain/range/reference rule-nak megfelel; accuracy azt, hogy a valós vagy authoritative source állapotát tükrözi. Syntactic validity nem bizonyít business accuracy-t, ehhez source reconciliation, domain sampling, owner review vagy external evidence kellhet.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [NIST Big Data Interoperability Framework](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-2-big-data-taxonomies)
