---
schema_version: 1
id: DBKB-INTG-0012
title: Integration Security
type: technology
primary_domain: data-integration
secondary_domains: [security-privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, avro]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-INTG-0007]
related: []
aliases: [secure data integration]
search_keywords: [TLS, SASL, ACL, secret, schema registry security]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000069, SRC-000070, SRC-000071]
acceptance_criteria: [Identity, transport, authorization, secrets and payload protection are covered]
---
# Integration Security

Integration securityben producer/consumer identity, TLS, broker/topic ACL, schema registry access, connector secret, source DB privilege, payload encryption és sensitive field masking szerepeljen. Debug logs, DLQ és replay artifact ugyanolyan data exposure path, mint a primary stream.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
