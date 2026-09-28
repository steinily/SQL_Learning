# Validation and QA

The QA pipeline separates content creation from verification.

Conceptual flow:

ARCHITECT → RESEARCH → WRITE → VALIDATE → AUDIT → FINAL QA → VERIFIED

## Validation dimensions

- sources
- factual claims
- syntax
- execution
- expected results
- dialect compatibility
- metadata
- links
- duplication
- contradictions
- terminology
- Docmost compatibility

## Severity

BLOCKER > CRITICAL > MAJOR > MINOR > INFO.

## Rules

- A writer cannot self-certify a document as fully verified.
- Execution verification requires actual execution.
- N/A must be explicit.
- Source conflict and uncertainty block full verification.
- Performance and security documents receive specialist review.
- Negative tests may expect failure and should validate stable error classes/codes where available.
