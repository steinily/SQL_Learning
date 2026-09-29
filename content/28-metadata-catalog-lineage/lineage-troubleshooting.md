---
schema_version: 1
id: DBKB-META-0013
title: Lineage Troubleshooting
type: troubleshooting
primary_domain: lineage
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openlineage, datahub]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0012]
related: []
aliases: [lineage failure diagnosis]
search_keywords: [missing lineage, stale metadata, duplicate edge, extractor failure]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000082]
acceptance_criteria: [Failure classification, source evidence and safe repair are described]
---
# Lineage Troubleshooting

Missing vagy hibás lineage oka lehet emitter/connector failure, unsupported operation, identity mismatch, schema parsing, ingestion lag, duplicate event vagy catalog merge conflict. Preserve-eld raw event/source run, timestamps, namespace és versiont; manual edge add csak provenance és review után történjen.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [DataHub Documentation](https://docs.datahub.com/)
