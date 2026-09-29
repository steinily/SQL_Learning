---
schema_version: 1
id: DBKB-DE-0014
title: Pipeline Scheduling
type: technology
primary_domain: data-engineering
secondary_domains: [automation, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-airflow]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-DE-0005]
related: []
aliases: [data pipeline scheduler]
search_keywords: [schedule, cron, timetable, catchup, backfill]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DE-0001]
source_ids: [SRC-000067]
acceptance_criteria: [Schedule, timezone, catchup, backfill and concurrency semantics are explained]
---
# Pipeline Scheduling

Pipeline schedule explicit timezone, interval, data interval, catchup/backfill, concurrency limit, retry és SLA/freshness policy alapján működjön. Scheduler success nem garantálja task output freshness-t; missed run, overlapping run és manual trigger külön state-ként kezelendő.

## Források
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
