---
schema_version: 1
id: DBKB-DARCH-0013
title: Data Architecture Troubleshooting
type: troubleshooting
primary_domain: data-architecture
secondary_domains: [operations, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [dcat, togaf]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0012]
related: [DBKB-OPS-0001]
aliases: [architecture incident diagnosis]
search_keywords: [data product incident, stale lineage, contract break, platform outage]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000094]
acceptance_criteria: [Architecture symptoms map to evidence, containment and governance remediation]
---
# Data Architecture Troubleshooting

**Data product stale:** inspect producer run, freshness SLO, lineage event, storage watermark és consumer cache; contain stale publication before changing schema. **Contract break:** identify version/consumer impact, activate compatibility path and record ADR/exception.

**Platform saturation:** compare tenant quota, queue/backlog, capacity and cost telemetry; throttle or isolate noisy neighbor, then verify downstream reconciliation. **Ownership gap:** stop irreversible change, assign accountable owner and update catalog/ADR before resuming.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
- [AWS Data Mesh Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-architectures/data-mesh.html)
