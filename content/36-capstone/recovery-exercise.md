---
schema_version: 1
id: DBKB-CAP-0038
title: Recovery Exercise
type: exercise
primary_domain: capstone
secondary_domains: [disaster-recovery, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, apache-kafka]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0037]
related: [DBKB-DR-0001]
aliases: [recovery lab]
search_keywords: [recovery exercise, restore, replay, RPO, RTO, reconciliation]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001, SRC-000087]
acceptance_criteria: [Learner executes or designs restore/failover/replay and correctness verification]
---
# Recovery Exercise

Szimulálj primary outage-ot és partial event publish-t. Válassz rollback/restore/failover/replay ágat known checkpoint, RPO/RTO, fencing és consumer impact alapján.

Rögzítsd backup/offset/LSN, commands/output, restore duration, count/checksum/quality/invariant és failback evidence-et. Recovery status csak post-validation és owner sign-off után PASS.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
