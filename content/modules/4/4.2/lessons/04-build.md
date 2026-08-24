# 4.2 — Authentication and phishing-resistant authenticators (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.

## Property (start here)

A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.

## Attacker capabilities and trust assumptions

- **Attacker:** Lookalike origin; intercepted password; fatigued user.
- **Trust:** Lab origin binding. Real authenticators later; this fixture models origin check.
Only webauthn + matching origin returns True.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def phishing_resistant(method: str, origin: str, expected: str) -> bool:
    if method != "webauthn":
        return False
    return origin == expected
```

## Why this restores the cell

WebAuthn origin/RP ID binding; do not call passwords resistant.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

HTML autocomplete=webauthn is not a ceremony.

WebAuthn does not authorize (1.2). Recovery paths can re-introduce phishable secrets (1.4, 4.1).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Step-up for export: still origin-bound?

## Residual risk

Users with only passwords — honest residual, not a slogan.
