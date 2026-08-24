# 3.1 — Assets, classification, and security requirements (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NIST CSF 2.0 Identify (final); ASVS 5.0.0 V14 (final); NIST Privacy Framework 1.0 (final). Classification is a property of a *field*, not a spreadsheet sticker.

## Property (start here)

Note bodies are Confidential. An application log line for note_read must not contain the body. Labels in Confluence do not enforce this.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator with log access; SIEM vendor; another tenant’s admin who can read shared observability.
- **Trust:** Local log sink. Real ELK is another TCB later (10.5).
**Forbidden outcome:** Confidential note body appears in a log line

**Authorized scope:** `labs/3.1/3.1-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable classify.py interpolates the body.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: Handler logs the event payload with the body.

## Vulnerable fixture (local)

```python
def log_event(event: str, note_body: str) -> str:
    return f"{event}: {note_body}"
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Body treated as debug context. |
| Impact | Confidential field in a lower-trust store. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/3.1/3.1-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Clinic notes vs appointment time: two classes, two sinks.

## Non-goals

No live-target instructions. Synthetic data only.
