# 4.2 — Authentication and phishing-resistant authenticators (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.

## Property (start here)

A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.

## Attacker capabilities and trust assumptions

- **Attacker:** Lookalike origin; intercepted password; fatigued user.
- **Trust:** Lab origin binding. Real authenticators later; this fixture models origin check.
**Forbidden outcome:** Password (or wrong-origin WebAuthn) counted as phishing-resistant

**Authorized scope:** `labs/4.2/4.2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable authn.py treats password as resistant.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: password method returns True for evil origin.

## Vulnerable fixture (local)

```python
def phishing_resistant(method: str, origin: str, expected: str) -> bool:
    return method in {"password", "otp", "webauthn"}
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Shared secret replayable at the wrong origin. |
| Impact | Attacker obtains session at the real app (then 1.2). |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/4.2/4.2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Step-up for export: still origin-bound?

## Non-goals

No live-target instructions. Synthetic data only.
