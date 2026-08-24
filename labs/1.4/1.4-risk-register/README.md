# Lab: 1.4-risk-register

**Module:** `1.4`  
**Authorized scope:** this directory only.  
**Invariant:** The SecureCollab account-recovery **confirm** control is not color-only or mouse-only (WCAG 2.2 as the web baseline). Inaccessible recovery is recorded as a **security** failure (lockout, coercion, or shared-admin workaround).  
**Root cause class:** trust / people (friction as bypass incentive)  
**Non-goals:** live IdPs, real user accounts, capturing real recovery emails.

## Reset

Restore `vulnerable/` and `fixed/` from git.

## Vulnerable behavior (local only)

Confirm is a green, mouse-only control with no accessible name. Residual risk is not “the scanner is yellow”; it is **users sharing a tenant-admin session**.

## Structural fix

Accessible name + keyboard operation. Color may remain as redundant encoding, not the only encoding.

## Verify

```bash
python3 -m pytest tests/test_recovery_a11y.py --impl vulnerable   # must fail
python3 -m pytest tests/test_recovery_a11y.py --impl fixed        # must pass
```

## Operate

If recovery is blocked, detect lockout tickets and have a **degrade** path that is still mediated (1.2), not “email the password.”

## Transfer

Coerced user: safety invariant from 1.1 — a recovery that only works with a second device they do not control fails that user-harm scenario.
