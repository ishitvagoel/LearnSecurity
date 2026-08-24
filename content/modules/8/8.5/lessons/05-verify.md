# 8.5 — Mobile verification and privacy (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** MASVS 2.1 + MASTG 2.0 (final); MASWE mapping; Mobile Top 10:2024 awareness only.

## Property (start here)

A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a Play Data safety form as the control.

## Attacker capabilities and trust assumptions

- **Attacker:** Crash-platform operator; another process reading logcat.
- **Trust:** Local crash_report(body).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Crash report contains the note body |
| Failure | Fail closed: Do not put bodies in exceptions; SDK filters; permission minimization |

Lab tests: `test_property.py` under `labs/8.5/8.5-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Crash report contains the note body`
- `--impl fixed`: **pass**

crash omits note body.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Web Sentry (10.5) same cell.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
