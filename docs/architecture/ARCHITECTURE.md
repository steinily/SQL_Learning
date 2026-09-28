# Architecture v1.0

Status: **FROZEN**

## Seven-layer model

1. Knowledge Base Content — canonical Markdown concepts, tutorials, recipes and cases.
2. Knowledge Graph — prerequisites, canonical relations and cross-topic relationships.
3. Research & Sources — claims, evidence, versions and provenance.
4. Demo Data Ecosystem — Atlas schemas, deterministic datasets, fixtures and scenarios.
5. Validation & QA — facts, SQL execution, results, dialects, metadata and links.
6. Governance & Metrics — scope, progress, coverage, debt, health and releases.
7. Delivery / Docmost — validated publishing projection.

## Validation classes

- **Deterministic:** executable or structurally provable checks.
- **Evidence-based:** claims supported by authoritative evidence.
- **Interpretive:** explanation quality, trade-offs and engineering guidance.

These classes must not be represented as equivalent verification.

## Canonical model

Each concept has one authoritative canonical location. Technology-specific documents describe implementation differences and link to canonical theory rather than duplicating it.

## Granularity

Use overview hubs, substantial core topics and specialist subtopics. Split when a topic is independently searchable, substantial, example-rich, dialect-sensitive, operationally important or frequently referenced. Documents above roughly 5,000 words are split candidates, not automatically split.

## Publishing

GitHub is canonical. Docmost is a projection. Manual Docmost changes are drift, not canonical edits.

## Change control

Frozen architecture changes require an ADR proposal, impact analysis and explicit acceptance.
