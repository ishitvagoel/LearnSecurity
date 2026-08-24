# 8.5 — Mobile verification and privacy (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** MASVS 2.1 + MASTG 2.0 (final); MASWE mapping; Mobile Top 10:2024 awareness only.

## Property (start here)

A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a Play Data safety form as the control.

## Attacker capabilities and trust assumptions

- **Attacker:** Crash-platform operator; another process reading logcat.
- **Trust:** Local crash_report(body).
**Forbidden outcome:** Crash report contains the note body

**Authorized scope:** `labs/8.5/8.5-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable crash.py includes body.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: secret in str(report).

## Vulnerable fixture (local)

```python
def crash_report(note_body):
    return {'stack': 'npe', 'note': note_body}
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Exception message includes the body. |
| Impact | Bodies at a vendor; maybe public if misbucketed. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/8.5/8.5-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Web Sentry (10.5) same cell.

## Non-goals

No live-target instructions. Synthetic data only.
