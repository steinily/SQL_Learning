.PHONY: validate test metrics qa audit atlas sql learn docmost docmost-bundle all

PYTHON ?= .venv/bin/python

validate:
	$(PYTHON) scripts/validate_repo.py

test:
	$(PYTHON) -m pytest -q

metrics:
	$(PYTHON) scripts/generate_metrics.py

qa:
	$(PYTHON) scripts/validate_repo.py --report validation/repository-latest.json

atlas:
	$(PYTHON) scripts/atlas_validate.py

sql:
	$(PYTHON) scripts/sql_harness.py --allow-destructive

learn:
	python3 scripts/learning_runner.py

audit:
	$(PYTHON) scripts/audit_documents.py

docmost:
	$(PYTHON) scripts/docmost_adapter.py --remote-state docmost/fixtures/empty-state.json

docmost-bundle:
	$(PYTHON) scripts/docmost_bundle.py --output-dir generated/docmost-import

all: test atlas sql audit qa metrics docmost
