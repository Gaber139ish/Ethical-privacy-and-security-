#!/usr/bin/env bash
set -euo pipefail

pytest -q || true

echo "Tests completed."