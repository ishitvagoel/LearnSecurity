# 3.1 — Assets, classification, and security requirements (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NIST CSF 2.0 Identify (final); ASVS 5.0.0 V14 (final); NIST Privacy Framework 1.0 (final). Classification is a property of a *field*, not a spreadsheet sticker.

## Property (start here)

Note bodies are Confidential. An application log line for note_read must not contain the body. Labels in Confluence do not enforce this.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator with log access; SIEM vendor; another tenant’s admin who can read shared observability.
- **Trust:** Local log sink. Real ELK is another TCB later (10.5).
log_event redacts body to 'redacted'/'confidential'.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def log_event(event: str, note_body: str) -> str:
    return f"{event}: [redacted-confidential]"
```

## Why this restores the cell

Structured logs with allow-listed fields; redact bodies.

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

uvicorn access logs will happily store query strings (4.3). FastAPI does not know Confidential.

Regex redaction misses encodings (2.1).

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Clinic notes vs appointment time: two classes, two sinks.

## Residual risk

Operators still see metadata (ids). That’s a different cell — document it.
