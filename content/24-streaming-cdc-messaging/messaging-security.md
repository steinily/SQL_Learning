---
schema_version: 1
id: DBKB-STREAM-0016
title: Messaging Security
type: technology
primary_domain: streaming
secondary_domains: [security-privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-kafka, debezium, apache-flink]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STREAM-0015]
related: []
aliases: [Kafka security]
search_keywords: [TLS, SASL, ACL, topic authorization, secret rotation]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STREAM-0001]
source_ids: [SRC-000069, SRC-000070]
acceptance_criteria: [Transport, identity, topic ACL, connector and payload protection are covered]
---
# Messaging Security

Messaging securityben broker/client TLS, authentication, topic/group ACL, connector/source privilege, schema registry access, secret rotation és payload privacy legyen. Least privilege a topic, group, transaction és admin operation scope-ra is vonatkozik; DLQ és replay artifactot ugyanúgy védeni kell.

## Források
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Debezium Documentation](https://debezium.io/documentation/)
