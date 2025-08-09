# Threat Model

## Assets
- Personal/sensitive data at rest and in transit
- Encryption keys (DEKs/KEKs)
- Analytics outputs (with DP noise)
- Metadata: access logs, identifiers, timing

## Adversaries
- Honest-but-curious storage nodes
- Malicious insiders with limited privileges
- Network attackers (MITM, replay)
- External attackers seeking data exfiltration

## Assumptions
- Strong client-side encryption is used before storage
- KMS/HSM protects KEKs with audit and rotation
- DP mechanisms enforce privacy budgets for analytics

## Attack Surfaces and Mitigations
- Data at rest: AEAD (AES-GCM or XChaCha20-Poly1305), integrity checks, versioning
- Data in transit: TLS 1.3, certificate pinning where applicable
- Key exposure: envelope encryption, short-lived tokens, rotation, dual control
- Metadata leakage: least-privilege access, coarse-grained identifiers, padded access patterns (where feasible)
- Query privacy: DP accounting, per-user budget, review of high-risk queries
- Node compromise: secret sharing/erasure coding across failure domains, tamper-evident logs

## Residual Risks
- Side channels and traffic analysis
- Configuration errors and operational mistakes
- Incomplete deletion in distributed networks

Risk acceptance and compensating controls are tracked in `SECURITY.md` and `COMPLIANCE.md`.