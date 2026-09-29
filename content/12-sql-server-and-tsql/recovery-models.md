---
schema_version: 1
id: DBKB-SS-0029
title: Recovery Models
type: concept
primary_domain: sql-server
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0028]
related: [DBKB-SS-0031]
aliases: [FULL, SIMPLE, BULK_LOGGED]
search_keywords: [SQL Server recovery model, full recovery, simple recovery]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Simple/full/bulk-logged recovery és log backup/RPO trade-offot adja]
---
# Recovery Models

SQL Server recovery model meghatározza transaction log backup és point-in-time recovery lehetőségeit. `SIMPLE`, `FULL` és `BULK_LOGGED` választás workload, RPO, log management és HA design alapján történjen.

## Források
- [Microsoft Learn — Recovery models](https://learn.microsoft.com/sql/relational-databases/backup-restore/recovery-models-sql-server)
