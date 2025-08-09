# ADR 0001: Initial Architecture and Cryptographic Approach

## Status
Accepted

## Context
We need a coherent, privacy-first architecture that can evolve. The current codebase includes research demos (DP, QKD, holographic memory) and storage sketches.

## Decision
- Use client-side AEAD and envelope encryption with an external KMS for stored objects
- Apply Differential Privacy to analytics outputs; track epsilon budgets
- Keep QKD and holographic memory as research demos only

## Consequences
- Clear separation between production-grade controls and research prototypes
- Easier compliance mapping and security reviews