---
schema_version: 1
id: DBKB-DQ-0004
title: Data Profiling
type: technology
primary_domain: data-quality
secondary_domains: [metadata]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [great-expectations, dbt]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DQ-0003]
related: []
aliases: [data profile]
search_keywords: [profiling, distribution, cardinality, outlier, schema inference]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DQ-0001]
source_ids: [SRC-000077, SRC-000079]
acceptance_criteria: [Profile dimensions, sampling caveats and rule derivation are explained]
---
# Data Profiling

Profiling distributiont, null rate-et, cardinalityt, min/maxot, patternt, outliert és schema shape-et tár fel; sample-based profile torzíthat. Profile outputot ne tekintsd quality verdictnek: expectation derivation, domain review, versioned baseline és drift comparison kell.

## Források
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [NIST Big Data Interoperability Framework](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-2-big-data-taxonomies)
