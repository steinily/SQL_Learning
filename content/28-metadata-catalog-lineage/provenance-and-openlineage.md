---
schema_version: 1
id: DBKB-META-0009
title: Provenance and OpenLineage
type: technology
primary_domain: lineage
secondary_domains: [interoperability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openlineage]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-META-0007]
related: []
aliases: [OpenLineage provenance]
search_keywords: [OpenLineage, job, run, dataset, facet, provenance]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000081]
acceptance_criteria: [OpenLineage entities/events and PROV concepts are scoped without overclaim]
---
# Provenance and OpenLineage

OpenLineage job/run/dataset/event/facet modellel interoperable lineage eventeket ír le; W3C PROV entity/activity/agent relációi általános provenance vocabulary-t adnak. Event emitter, namespace, run identity, schema/quality facets, transport és consumer support target implementationen validálandó.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
