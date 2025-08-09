# Privacy-Preserving AI System

A conceptual system that explores how to build AI applications that respect privacy by design. The current prototype combines:

- Decentralized or distributed data storage
- Differential Privacy (DP) for analytics
- Quantum Key Distribution (QKD) simulation (research/demo)
- Holographic memory encoding simulation (research/demo)

This repository currently includes static documentation pages and Python concept demos under `Src/`.

## Quickstart

- Prerequisites: Python 3.10+
- Optional: create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
# Runtime deps are optional for now; install if you plan to run the concept demos
# pip install -r requirements.txt
```

- Lint and tests (no code changes required):

```bash
bash scripts/lint.sh
bash scripts/test.sh
```

## Repository layout

- `Index.html`, `About.html`, `Technology.html`, `Privacy.html`, `Documentation.html`: Project overview pages
- `Src/`: Concept Python demos
  - `AIcore.py`: Differential Privacy (SmartNoise) demo
  - `Database.py`: Decentralized storage sketches (Cassandra/IPFS)
  - `QKD.py`: QKD simulation (Qiskit)
  - `Holographic_memory.py`: Holographic encoding demo (NumPy)
- `docs/`: Architecture, roadmap, ADRs
- `.github/workflows/`: CI configuration
- `scripts/`: Developer scripts (lint, test)

## Key documents

- See `ARCHITECTURE.md` for a high-level system view
- See `THREAT_MODEL.md` for adversaries, assets, and mitigations
- See `PRIVACY.md` and `COMPLIANCE.md` for privacy and governance posture
- See `SECURITY.md` for crypto/key management approach

## Notes

- The Python demos in `Src/` are research prototypes and may require additional dependencies and hardware to run. They are not executed by CI.
- No changes have been made to existing code; all files added here are purely additive.