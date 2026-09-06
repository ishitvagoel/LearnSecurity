# SecureCollab Phase 1 — classification and log sinks

Design stub for Module 3.1. Not a production SIEM.

## Freeze

- Local `log_event` fixture. Synthetic body string only.
- No real PII, no production log drain.

## Field × sink

Confidential bodies may live in the note table. They must not appear in application logs. Note ids are a different cell.

## Tests

The forbidden substring is the evidence. A spreadsheet is not.
