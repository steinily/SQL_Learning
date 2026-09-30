---
schema_version: 1
id: DBKB-CAP-0085
title: V1 Capstone Assessment
type: exercise
primary_domain: capstone
secondary_domains: [learning, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka, openmetadata, openapi]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0084]
related: [DBKB-CAP-0001]
aliases: [V1 final assessment]
search_keywords: [capstone assessment, end to end, architecture, data, reliability, evidence]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000080, SRC-000092, SRC-000095]
acceptance_criteria: [Assessment integrates modeling, SQL, operations, data engineering, contracts, governance and evidence]
---
# V1 Capstone Assessment

Tervezd és validáld egy order/customer platform end-to-end solutionjét: relational schema/query/transaction; integration/streaming contract; quality/lineage/master data; security/operations/recovery; architecture ADR; cloud/NoSQL/distributed trade-off.

Deliverables: context/ERD, DDL/query/tests, contracts, pipeline/quality/lineage evidence, IAM/threat controls, SLO/RPO/RTO, runbooks, migration/rollback, cost assumptions, learning reflection és final decision log.

Assessment csak akkor PASS, ha minden claim source-verified, minden execution-verified állítás tényleges outputtal bizonyított, a validation/audit gate zöld és a residual risk explicit.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [OpenLineage Documentation](https://openlineage.io/docs/)
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
