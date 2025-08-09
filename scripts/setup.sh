#!/usr/bin/env bash
set -euo pipefail

PY=${PYTHON:-python3}
$PY -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-dev.txt || true
# Runtime deps are optional; uncomment to install
# pip install -r requirements.txt

echo "Setup completed. Activate with: source .venv/bin/activate"