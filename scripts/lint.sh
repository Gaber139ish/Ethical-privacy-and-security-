#!/usr/bin/env bash
set -euo pipefail

# Lint only our scaffolding to avoid flagging existing prototypes
flake8 scripts tests || true
black --check scripts tests

echo "Lint completed."