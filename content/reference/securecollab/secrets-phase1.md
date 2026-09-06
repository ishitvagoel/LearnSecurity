# SecureCollab Phase 1 — application secret lifecycle

Design stub for Module 5.3. Not a production KMS.

## Freeze

- Local `auth(presented, current)`. Disposable `sk-lab-hardcoded`.
- No live vault.

## Current is the only acceptor

After rotation, the hardcoded default must fail. Missing current denies. Application secrets are not user passwords and not public ids.

## Tests

`auth("sk-lab-hardcoded", current="rotated-now")` is false. Vault brand names are not evidence.
