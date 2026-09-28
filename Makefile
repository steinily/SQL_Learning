.PHONY: validate test

validate:
	python scripts/validate_repo.py

test:
	pytest -q
