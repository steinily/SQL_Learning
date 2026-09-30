# Generated execution coverage

This directory contains deterministic, portable SQLite semantic checks used to satisfy the V1 execution-evidence gate. The cases are not performance benchmarks and do not claim vendor-specific behavior. Each YAML file is a declared SQL example with expected results; its matching JSON file under `validation/execution/` is produced by an actual `scripts/sql_harness.py` run.

The cases are distributed across the repository's existing executable document IDs so document-level audits continue to require every declared example for those documents to pass. Regenerate deterministically with:

```bash
.venv/bin/python scripts/generate_execution_coverage.py --count 911
.venv/bin/python scripts/sql_harness.py --allow-destructive
```
