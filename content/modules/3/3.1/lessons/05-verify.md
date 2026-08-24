# 3.1 — Assets, classification, and security requirements (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NIST CSF 2.0 Identify (final); ASVS 5.0.0 V14 (final); NIST Privacy Framework 1.0 (final). Classification is a property of a *field*, not a spreadsheet sticker.

## Property (start here)

Note bodies are Confidential. An application log line for note_read must not contain the body. Labels in Confluence do not enforce this.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator with log access; SIEM vendor; another tenant’s admin who can read shared observability.
- **Trust:** Local log sink. Real ELK is another TCB later (10.5).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Confidential note body appears in a log line |
| Failure | Fail closed: Structured logs with allow-listed fields; redact bodies |

Lab tests: `test_property.py` under `labs/3.1/3.1-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Confidential note body appears in a log line`
- `--impl fixed`: **pass**

body not in line; marker present.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Clinic notes vs appointment time: two classes, two sinks.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
