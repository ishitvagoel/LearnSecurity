# 3.1 — Assets, classification, and security requirements (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST CSF 2.0 Identify (final); ASVS 5.0.0 V14 (final); NIST Privacy Framework 1.0 (final). Classification is a property of a *field*, not a spreadsheet sticker.

## Property (start here)

Note bodies are Confidential. An application log line for note_read must not contain the body. Labels in Confluence do not enforce this.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator with log access; SIEM vendor; another tenant’s admin who can read shared observability.
- **Trust:** Local log sink. Real ELK is another TCB later (10.5).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Secret scanning on log streams; DLP on the sink. |
| Signal (no bodies) | log_redaction_miss alerts; purge runbook. |
| Revoke / recover | Purge matching logs; rotate if tokens present. |
| Residual | Operators still see metadata (ids). That’s a different cell — document it. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/3.1/3.1-lab`.

## Transfer

Clinic notes vs appointment time: two classes, two sinks.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
