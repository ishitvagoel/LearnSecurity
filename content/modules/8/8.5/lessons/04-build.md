# 8.5 — Mobile verification and privacy (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** MASVS 2.1 + MASTG 2.0 (final); MASWE mapping; Mobile Top 10:2024 awareness only.

## Property (start here)

A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a Play Data safety form as the control.

## Attacker capabilities and trust assumptions

- **Attacker:** Crash-platform operator; another process reading logcat.
- **Trust:** Local crash_report(body).
secret not in report.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def crash_report(note_body):
    return {'stack': 'npe', 'note': '[redacted]'}
```

## Why this restores the cell

Do not put bodies in exceptions; SDK filters; permission minimization.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

Firebase Crashlytics “automatic” will ship whatever you log.

Play Data safety form is disclosure, not redaction.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Web Sentry (10.5) same cell.

## Residual risk

Vendor as processor — contract + 5.1.
