# Lab: 2.3-browser-policy

**Module:** `2.3` — Browser security model
**Authorized scope:** Local application origin only
**Invariant:** Claims about this concern must be property-shaped (attacker, trust, time horizon, evidence) and name SecureCollab assets.
**Root cause class:** trust / authority / parser / state / resource (module-specific)
**Non-goals:** live targets, real PII, weaponized learner-facing payloads.

## Reset

Replace `vulnerable/` or `fixed/` claim files from git. Do not keep learner secrets.

## Vulnerable behavior (local only)

The vulnerable claim is a mechanism slogan. Tests must **fail**. This is a local fixture only.

Browser policy matrix and local cookie/CORS fixture

## Structural fix

The fixed claim states a system-specific property plus attacker, trust, time horizon, and evidence. A scanner-only or denylist response is insufficient.

## Verify

- Happy path: fixed claim passes `--claim`
- Negative: vulnerable claim fails `--claim`
- No network calls; synthetic data only

## Operate

If the invariant is not absolute, record what you would log, alert on, revoke, or restore.

## Transfer

Add a new principal or object and rewrite the claim without a Top 10 name as the property.
