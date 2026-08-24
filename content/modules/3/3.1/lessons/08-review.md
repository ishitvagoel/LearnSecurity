# 3.1 — Assets, classification, and security requirements (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NIST CSF 2.0 Identify (final); ASVS 5.0.0 V14 (final); NIST Privacy Framework 1.0 (final). Classification is a property of a *field*, not a spreadsheet sticker.

## Property (start here)

Note bodies are Confidential. An application log line for note_read must not contain the body. Labels in Confluence do not enforce this.

## Attacker capabilities and trust assumptions

- **Attacker:** Operator with log access; SIEM vendor; another tenant’s admin who can read shared observability.
- **Trust:** Local log sink. Real ELK is another TCB later (10.5).
Review `labs/3.1/3.1-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/3.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): logger.info('read %s', note.body)
- Seeded smell (label it yourself): Classification spreadsheet with no test
- Seeded smell (label it yourself): Debug=True in a “staging” that shares prod data
- Seeded smell (label it yourself): Exception middleware dumps request body

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- If we classified it, it is protected
- Logs are internal so safe
- Privacy policy equals redaction

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Clinic notes vs appointment time: two classes, two sinks.
