---
schema_version: 1
id: DBKB-META-0015
title: Metadata and Lineage Exercise
type: exercise
primary_domain: metadata
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openlineage, datahub]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-META-0014]
related: []
aliases: [metadata exercise]
search_keywords: [catalog exercise, lineage, ownership, quality, deprecation]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-META-0001]
source_ids: [SRC-000080, SRC-000081, SRC-000082]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Metadata and Lineage Exercise

Készíts metadata onboarding tervet egy source database → pipeline → warehouse dataset → BI metric láncra. Rögzíts technical/business metadata-t, owner/stewardot, OpenLineage eventet, catalog quality checket, security tags-et, lineage gap repairt és deprecationt; execution-verified csak valódi futtatás után használható.

## Források
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [DataHub Documentation](https://docs.datahub.com/)
