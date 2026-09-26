# Lab: 3.1-lab

**Module:** `3.1`
**Authorized scope:** this directory only. Local FastAPI fixture; synthetic note bodies and session tokens; no production log drain, no real people's data, no live clinic or tenant.
**Tier:** 2 (component). A real FastAPI request/response cycle through `fastapi.testclient.TestClient`, with server-side state (`NOTES`, two sinks: `_LOG_LINES` and `_ERROR_DUMPS`) that persists across calls within one test and resets between tests — see `lab-realism.mdc`.

**Invariant (C1):** A field classified Confidential may reach a sink only when that sink's own documented policy allows that level; a classification label with no sink check is not a control.
**Invariant (C2):** An authority artifact (the session token) is classified at least as sensitively as the content it gates, and both sinks deny it identically to the note body.
**Invariant (C4):** A field this fixture's classification table has never named defaults to the most restrictive level, not the least — silence is not "public."
**Root cause class:** trust (a sink that accepts whatever context it is handed) and a missing fail-safe default (an unrecognized field treated as safe instead of as unresolved risk).
**Non-goals:** cross-company authorization (owned by module 4.4's `can_read` matrix — this fixture's session lookup identifies a caller's company for logging context only, and does not gate which notes that caller may read); production log pipelines; exception middleware or slow-query logs outside `log_event`/`write_error_dump`; encryption at rest (module 5.3).

## Reset

No persistent state between tests. `conftest.py` loads a fresh module and calls `reset()` before every test. Optional: `git checkout -- labs/3.1/3.1-lab`.

## Vulnerable behavior (local only)

`log_event` and `write_error_dump` both accept every field of the context dictionary they are given and render it verbatim. `CLASSIFICATION` is present but never read by either function. See `vulnerable/SECURITY.md`.

## Structural fix

Both sinks call `_redact(context, sink)` before rendering. `_redact` looks up each field's level in `CLASSIFICATION`, defaulting an unrecognized field to `confidential`, and keeps only the fields whose level appears in that sink's `SINK_POLICY`; everything else becomes a `[redacted-<level>]` marker. See `fixed/SECURITY.md`.

## Verify

```bash
python3 -m pytest labs/3.1/3.1-lab/tests --impl vulnerable   # 7 of 9 fail
python3 -m pytest labs/3.1/3.1-lab/tests --impl fixed         # 9 of 9 pass
```

If `fastapi`/`httpx` are not already installed: `pip install -r labs/3.1/3.1-lab/requirements.txt`.

Nine tests in `test_property.py`: the two forbidden outcomes (note body and session token excluded from the application log — C1, C2), a boundary case showing the token is denied by a *second*, independently-reached sink (the error dump — C2), a malformed/failure-path case proving the error dump still names which note and company failed without naming the token (C5), two normal-case tests confirming redaction does not become "log nothing" (allowed metadata still present; an absent optional header does not break logging — C3), a fail-safe-default case proving an unrecognized field is denied by default rather than allowed by default (C4), and two anti-fake tests.

**Anti-fake tests are not decoration.** `test_anti_fake_fresh_secret_not_a_literal_match` uses a freshly generated, never-hardcoded body string, defeating a fake fix that special-cases the literal `"tenant-A-secret-body"` instead of building a real per-field mechanism. `test_anti_fake_redaction_is_not_a_canned_line` reads two different notes and requires the log to still distinguish them by `note_id`, defeating a fake fix that makes `log_event` always append one fixed literal line regardless of input — a cheat that would otherwise pass every test that only checks for a *secret's* absence. `test_unclassified_field_defaults_to_redacted` doubles as a third anti-fake check: it defeats a fix that hardcodes exactly two denied field names (`note_body`, `session_token`) instead of a real table-driven, default-deny allow-list, by proving a third, never-named field is denied too.

## Operate

Signal a redaction miss — a sink emitting a field whose level is not in that sink's policy — as `log_redaction_miss reason=confidential_field event=<event> sink=<sink>`, never carrying the denied value itself. See [`lessons/06-operate.md`](../../../content/modules/3/3.1/lessons/06-operate.md).

## Transfer

A clinic booking card where chart text and appointment time sit on one record. Prompt only; do not leave this directory. See [`lessons/07-transfer.md`](../../../content/modules/3/3.1/lessons/07-transfer.md).
