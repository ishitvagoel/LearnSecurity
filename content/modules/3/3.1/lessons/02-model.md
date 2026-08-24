# 3.1 — Assets, classification, and security requirements (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NIST CSF 2.0 Identify (final); ASVS 5.0.0 V14 (final); NIST Privacy Framework 1.0 (final). Classification is a property of a *field*, not a spreadsheet sticker.

## Property (start here)

Note bodies are Confidential. An application log line for note_read must not contain the body. Labels in Confluence do not enforce this.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator with log access; SIEM vendor; another tenant’s admin who can read shared observability.
- **Trust:** Local log sink. Real ELK is another TCB later (10.5).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | App logger, operator, SIEM |
| Objects | note body, log line, classification tag |
| Actions | log_event, read_logs |
| Channels | stdout, log drain |
| TCB | Redaction in the logging API used by handlers. |
| Untrusted | print(), f-strings, APM capture, exception repr |
| State / time | Logs retained 30 days after the note is deleted (5.1). |
| 1.1 cell | Confidentiality + privacy of the body. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| handler | body | log | deny |
| handler | note_id | log | allow |
| operator | logs | read | meta-only |
| SIEM vendor | body | index | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/3.1/3.1-lab` file `classify.py`.

## Transfer

Clinic notes vs appointment time: two classes, two sinks.

## Residual risk

Operators still see metadata (ids). That’s a different cell — document it.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
