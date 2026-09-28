# Architecture Decision Register

Architecture version: **1.0**  
Status: **FROZEN**

Accepted decisions:

| ADR | Decision |
|---|---|
| ADR-001 | GitHub is the canonical source of truth |
| ADR-002 | Docmost is a publishing/search projection |
| ADR-003 | Use a canonical topic model |
| ADR-004 | Use hybrid document granularity |
| ADR-005 | Stable document IDs are independent of paths |
| ADR-006 | Use a strict versioned metadata schema |
| ADR-007 | Maintain typed knowledge-graph relations |
| ADR-008 | Prerequisite graph is distinct from related-topic graph |
| ADR-009 | Use an explicit source/evidence hierarchy |
| ADR-010 | Model knowledge is not verification evidence |
| ADR-011 | Separate deterministic, evidence and interpretive validation |
| ADR-012 | Execute SQL examples where feasible |
| ADR-013 | Validate expected results where applicable |
| ADR-014 | Support expected-error/negative tests |
| ADR-015 | Validation is dialect-aware |
| ADR-016 | Documentation is version-aware |
| ADR-017 | Major technology releases trigger targeted revalidation |
| ADR-018 | Content creation and final verification are separate duties |
| ADR-019 | Logical reviewer roles need not be separate physical agents |
| ADR-020 | Work Packages are the execution unit |
| ADR-021 | Automation cannot silently expand accepted scope |
| ADR-022 | Rework loops are bounded; unresolved work escalates |
| ADR-023 | Atlas Manufacturing is the canonical synthetic demo ecosystem |
| ADR-024 | Use both micro fixtures and integrated Atlas fixtures |
| ADR-025 | Demo data generation is deterministic |
| ADR-026 | Schemas, datasets and fixtures are versioned |
| ADR-027 | Scenarios are first-class reusable objects |
| ADR-028 | New demo structures require teaching value |
| ADR-029 | Progress is weighted deterministically |
| ADR-030 | Baseline scope, current scope and backlog are distinct |
| ADR-031 | Project Health and Release Readiness are distinct |
| ADR-032 | Metrics never replace explicit release gates |
| ADR-033 | QA tooling itself requires tests |
| ADR-034 | Changes trigger impact analysis |
| ADR-035 | Generated artifacts are not authoritative authored content |
| ADR-036 | Generate indexes/glossary projections where practical |
| ADR-037 | Docmost mapping uses stable document IDs |
| ADR-038 | Publishing supports dry-run |
| ADR-039 | Silent bulk deletion is prohibited |
| ADR-040 | Detect GitHub/Docmost drift |
| ADR-041 | The KB uses versioned releases |
| ADR-042 | Work requires a Definition of Ready |
| ADR-043 | Documents, domains and releases have Definitions of Done |
| ADR-044 | BLOCKED and uncertainty states are valid outcomes |
| ADR-045 | Unsupported claims cannot become VERIFIED |
| ADR-046 | The manifest is machine-readable |
| ADR-047 | Automation structures are schema-first and versioned |
| ADR-048 | Generated builds should be reproducible |
| ADR-049 | Explanations are Hungarian; technical terminology remains English |
| ADR-050 | Code, identifiers and vendor terms remain in original syntax |
| ADR-051 | Runnable examples must be copyable |
| ADR-052 | Example dependencies must be explicit |
| ADR-053 | Destructive examples are opt-in |
| ADR-054 | Benchmarks distinguish MEASURED, SIMULATED and ILLUSTRATIVE |
| ADR-055 | Case studies declare REAL, ANONYMIZED or SYNTHETIC provenance |
| ADR-056 | Invented production measurements/incidents are prohibited |
| ADR-057 | Uncertainty is explicit |
| ADR-058 | Track Knowledge Debt |
| ADR-059 | Track Technical Debt separately |
| ADR-060 | Release debt is governed by severity and gates |

A decision is changed by a new ADR that supersedes the old decision; accepted history is not silently rewritten.
