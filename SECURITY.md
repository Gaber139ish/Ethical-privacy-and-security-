# Security Overview

## Cryptography
- AEAD for data objects: AES-GCM or XChaCha20-Poly1305
- Hashing: SHA-256/512; HMAC for message authentication where needed
- PQC readiness: plan for Kyber (KEM) and Dilithium (signatures) when libraries stabilize

## Key Management
- Envelope encryption: per-object DEKs wrapped by KEK in KMS/HSM
- Rotation: periodic and on-demand; enforce key versioning
- Access: short-lived scoped tokens; break-glass procedures logged and reviewed

## Operational Security
- Principle of least privilege for services and humans
- Signed releases; SBOM and dependency scanning in CI
- Incident response runbooks and security contacts in repository