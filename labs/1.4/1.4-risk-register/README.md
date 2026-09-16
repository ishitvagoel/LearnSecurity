# Lab: 1.4-risk-register

**Module:** `1.4`
**Authorized scope:** this directory only. No browser, no live login provider, no real mailbox.
**Invariant (C2):** The SecureCollab account-recovery **confirm** control is not color-only or mouse-only, and it must declare positive keyboard support rather than merely omit `mouse_only`. Inaccessible recovery is recorded as a **security** failure (lockout, coercion, or a shared-admin workaround), not a UI nit.
**Root cause class:** trust / people — the checker verified the absence of one bad flag instead of the presence of a good guarantee, which is fail-open by omission.
**Tier:** 1 (predicate). `recovery_confirm_control()` and `is_usable_accessible()` are pure functions over a small declarative dict; there is no request cycle or persisted state this module's claim depends on, so a component lab would add process without adding teaching value here. See `lab-realism.mdc`.
**Non-goals:** live IdPs, real user accounts, capturing real recovery emails, a full accessibility audit of the product.

## Reset

No persistent state. Re-run pytest. Optional: `git checkout -- labs/1.4/1.4-risk-register`.

## Vulnerable behavior (local only)

Confirm is a green, mouse-only control with no accessible name. The checker itself has a second, quieter defect: it never asks for positive evidence of keyboard support, so a control that is silent on the question (not flagged `mouse_only`, but no `keyboard` key either) is incorrectly accepted. Residual risk is not "the scanner is yellow"; it is **users sharing a tenant-admin session** or pasting recovery codes into chat because the button they were given does not work.

## Structural fix

Two changes, not one: the control declares `keyboard: True` (positive evidence), and the checker requires that declaration rather than merely checking that `mouse_only` is unset. A whitespace-only name is also rejected — `not "  "` is `False` in Python, so a naive truthiness check would accept a name that announces nothing.

## Verify

```bash
python3 -m pytest tests/test_recovery_a11y.py --impl vulnerable   # 3 of 6 fail
python3 -m pytest tests/test_recovery_a11y.py --impl fixed        # 6 of 6 pass
```

From the repository root:

```bash
python3 -m pytest labs/1.4/1.4-risk-register/tests --impl vulnerable
python3 -m pytest labs/1.4/1.4-risk-register/tests --impl fixed
```

Six tests: the module's forbidden outcome; the color-only-without-name boundary; the missing-keyboard-flag boundary (the checker's own gap); the whitespace-only-name malformed input; and a two-test anti-fake pair that calls the checker directly on constructed input, independent of either module's factory, so a fake repair that hardcodes the checker to always return `True` (or always `False`) cannot pass by having the object and the checker agree with each other.

## Operate

If recovery is blocked, detect lockout tickets and open a **degrade** path that is itself still checked (C5) — not "email the password" and not "have support read the code aloud."

## Transfer

Coerced user: the safety invariant from Module 1 — a recovery that only works with a second device the user does not control fails that user-harm scenario. See `lessons/07-transfer.md` for the clinic and banking cases.
