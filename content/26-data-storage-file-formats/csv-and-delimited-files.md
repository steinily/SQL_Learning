---
schema_version: 1
id: DBKB-STOR-0008
title: CSV and Delimited Files
type: technology
primary_domain: data-storage
secondary_domains: [data-integration]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [csv]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0001]
related: []
aliases: [delimited text files]
search_keywords: [CSV, delimiter, quote, escape, header, encoding]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000076]
acceptance_criteria: [CSV ambiguity, encoding, quoting and schema contract risks are covered]
---
# CSV and Delimited Files

CSV/delimited text könnyen cserélhető, de delimiter, quote, escape, newline, header, encoding, null és type inference ambiguity-t okoz. Production ingestionhez manifest, explicit schema, checksum, row/error policy és producer/consumer test szükséges; „CSV readable” nem contract.

## Források
- [RFC 8259 — JSON data interchange context](https://www.rfc-editor.org/rfc/rfc8259)
