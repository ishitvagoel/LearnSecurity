# 4.2 — Authentication and phishing-resistant authenticators (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.

## Property (start here)

A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.

## Attacker capabilities and trust assumptions

- **Attacker:** Lookalike origin; intercepted password; fatigued user.
- **Trust:** Lab origin binding. Real authenticators later; this fixture models origin check.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Password (or wrong-origin WebAuthn) counted as phishing-resistant |
| Failure | Fail closed: WebAuthn origin/RP ID binding; do not call passwords resistant |

Lab tests: `test_property.py` under `labs/4.2/4.2-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Password (or wrong-origin WebAuthn) counted as phishing-resistant`
- `--impl fixed`: **pass**

password+evil False; webauthn+evil False.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Step-up for export: still origin-bound?

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
