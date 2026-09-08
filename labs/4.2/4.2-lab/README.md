# Lab 4.2 — origin binding, not “we have MFA”

**Module:** `4.2`
**Authorized scope:** this directory only. Local course fixture. No live phishing sites.
**Invariant:** A password or OTP at a lookalike origin is not phishing-resistant. WebAuthn at the wrong origin must fail. Passwords at the real origin remain a labeled residual.
**Root cause class:** trust (shared secret replayable at the wrong origin)
**Non-goals:** live targets, real credentials, weaponized kits.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/4.2/4.2-lab`, then run `git restore --source=HEAD -- labs/4.2/4.2-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`phishing_resistant` returns true for `password`, `otp`, and `webauthn` and ignores origin. Forbidden outcome: password (or wrong-origin WebAuthn) counted as phishing-resistant.

## Structural fix

Return true only when `method == "webauthn"` and `origin == expected`.

## Verify

```
python3 -m pytest tests --impl vulnerable
python3 -m pytest tests --impl fixed
```

From repo root:

```
python3 -m pytest labs/4.2/4.2-lab/tests --impl vulnerable
python3 -m pytest labs/4.2/4.2-lab/tests --impl fixed
```

The first command must fail. The second must pass.

## Operate

Signal: `webauthn_fail_origin` / `not_phishing_resistant` with method; never a password. Revoke sessions if a password was used.

## Transfer

Clinic staff SSO; step-up for export. Prompt only; do not leave this directory.
