# 3.1 — Assets, classification, and security requirements (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST CSF 2.0 Identify (final); ASVS 5.0.0 V14 (final); NIST Privacy Framework 1.0 (final). Classification is a property of a *field*, not a spreadsheet sticker.

## Property (start here)

Note bodies are Confidential. An application log line for note_read must not contain the body. Labels in Confluence do not enforce this.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator with log access; SIEM vendor; another tenant’s admin who can read shared observability.
- **Trust:** Local log sink. Real ELK is another TCB later (10.5).
**Mechanism (not the property):** uvicorn access logs will happily store query strings (4.3). FastAPI does not know Confidential.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 3.1 |
|---|---|
| Root cause | Body treated as debug context. |
| Preconditions | Handler logs the event payload with the body. |
| Impact (1.1 cell) | Confidentiality + privacy of the body. — Confidential field in a lower-trust store. |
| Prevention | Structured logs with allow-listed fields; redact bodies. |
| Detection | Secret scanning on log streams; DLP on the sink. |
| Recovery | Purge matching logs; rotate if tokens present. |

## Framework defaults vs application guarantees

uvicorn access logs will happily store query strings (4.3). FastAPI does not know Confidential.

## Mechanism limits and bypasses

Regex redaction misses encodings (2.1).

Error traces, slow-query logs, full-packet APM.

## Residual risk

Operators still see metadata (ids). That’s a different cell — document it.

## Practice

List every sink that might see a body (app, DB logs, CDN, mobile crash — 8.5).

Run `labs/3.1/3.1-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Clinic notes vs appointment time: two classes, two sinks.

EHR-lite booking card.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
