---
schema_version: 1
id: DBKB-INTG-0013
title: Integration Observability
type: technology
primary_domain: data-integration
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, opentelemetry]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0011]
related: []
aliases: [integration telemetry]
search_keywords: [throughput, lag, offset, error rate, consumer lag]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070]
acceptance_criteria: [Throughput, lag, errors, offsets, freshness and trace correlation are defined]
---
# Integration Observability

Integration telemetry mérje throughput, consumer lag, offset age, processing latency, retry/DLQ rate, schema error, duplicate rate, freshness és reconciliation status-t. Correlate-eld source event ID, partition/offset, connector task és downstream trace context alapján; unbounded payload labelt ne exportálj.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
