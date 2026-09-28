# Repository Layout Contract

```text
/
├── CODEX.md
├── README.md
├── PROJECT_STATUS.md
├── content/                 # canonical authored KB
├── manifest/                # frozen baseline and document registries
├── schemas/                 # versioned machine contracts
├── research/                # research packages/evidence
├── validation/              # machine QA reports
├── atlas/                   # synthetic demo ecosystem
├── scenarios/               # reusable scenarios
├── work-packages/           # bounded execution units
├── qa/                      # QA policy/config
├── metrics/                 # metrics definitions/raw snapshots
├── generated/               # generated projections; not hand-authored
├── docmost/                 # publishing adapter/contracts
├── scripts/                 # validators/generators
├── tests/                   # tooling and content-validation tests
└── docs/architecture/       # architecture and ADRs
```

## Content layout

Codex may create module directories such as `content/01-foundations/`, `content/02-sql-fundamentals/`, etc. Stable IDs, not paths, are identity.

## Generated content

Generated artifacts must include a clear generated marker and must be reproducible from canonical repository state.

## Machine state

Machine-readable state is preferred over parsing prose dashboards. Markdown status pages are projections of structured state.
