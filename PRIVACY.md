# Privacy Posture

## Data Minimization
- Collect only necessary fields; classify data by sensitivity
- Pseudonymize identifiers when possible

## Differential Privacy Policy
- Define epsilon budgets per dataset/task
- Use privacy accounting to track cumulative loss
- Prefer aggregations; disallow raw record joins/exports

## User Rights and Controls
- Consent tracking and purpose limitation
- Data subject requests (access, deletion, portability) workflow

## Retention and Deletion
- Time-bounded retention with documented schedules
- Cryptographic erasure by destroying DEKs; verify deletion where feasible

## Transparency and Auditability
- Maintain access logs for data and keys
- Document DP parameters in result metadata when appropriate