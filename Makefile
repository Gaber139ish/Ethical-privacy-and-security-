PY?=python3
VENV=.venv

.PHONY: setup lint test

setup:
	$(PY) -m venv $(VENV); . $(VENV)/bin/activate; pip install -U pip; pip install -r requirements-dev.txt || true

lint:
	bash scripts/lint.sh

test:
	bash scripts/test.sh