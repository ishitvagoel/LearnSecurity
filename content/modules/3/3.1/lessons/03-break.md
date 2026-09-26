# Local fixture: a classification table nobody reads

**Kind:** mechanism-lab
**Loop step:** 3 Break

## Starting from what has to be true for the leak to happen

Before running anything, work out the preconditions this failure needs, because a failure you can predict is a failure you actually understand, and a failure you can only observe after the fact is one you will misdiagnose the next time it looks slightly different. Three things have to hold at once for a note body or a session token to reach a log line. First, a function somewhere has to build a dictionary or an object containing the field — this is unavoidable and not itself a defect, because a handler has to know the note body and the caller's token to do its job at all. Second, that same function, or one it calls, has to render some or all of that structure into a string destined for a sink. Third — and this is the actual defect, not a precondition shared with every correct implementation — nothing between the second step and the sink's output has to check the field's classification level against what that specific sink is allowed to carry. Remove any one of the three and there is no leak: remove the first, and the handler cannot function; remove the second, and nothing is ever rendered; remove the third's *absence* — that is, add the check — and this lesson's lab moves from `vulnerable/` to `fixed/`.

`vulnerable/app.py`'s `log_event` satisfies exactly this precondition set. It receives a `context` dictionary already containing `note_body` and `session_token`, because the caller (`read_note`) had to look both up to do its job. It renders every key-value pair in that dictionary into one string. And it never opens `CLASSIFICATION`, the table sitting a few lines above it in the same file, to decide whether any given key belongs in that string. The exact line is:

```python
rendered = " ".join(f"{key}={value}" for key, value in context.items())
```

`context.items()` iterates over every field the caller happened to include, with no filter, no allow-list, no reference to any classification table anywhere in scope. This is the step where the property from [`lessons/01-property.md`](01-property.md) goes false: not at the moment the handler looked up the note body — it had to, to answer the request — but at this one line, where "every field the caller built" becomes "every field the line contains," with nothing in between asking whether it should.

## Where you may practice

Run this only inside `labs/3.1/3.1-lab/`. `sess-alice` is a fixture session token and `tenant-A-secret-body` is a fixture note body; neither is a real credential or a real person's data, and the lab's `reset()` clears all state before every test.

```text
python3 -m pytest labs/3.1/3.1-lab/tests --impl vulnerable
```

## What the failing tests show, and what a passing setup would hide

Two tests fail for the reason this lesson names, and the distinction between them matters. `test_note_body_excluded_from_application_log` posts a read for note `n1` and then asks the fixture's own `/internal/log-lines` endpoint what actually got written; the fixture literal `tenant-A-secret-body` is present in the returned line, so the assertion that it is absent fails. `test_session_token_excluded_from_application_log` runs the identical read and checks for `sess-alice` in the same output; it fails for the same underlying reason — one function, one missing check, two different fields caught by the same absence. A third test, `test_session_token_excluded_from_error_dump`, deliberately requests a note id that does not exist (`missing-note`), which routes through `write_error_dump` instead of `log_event` — a different function, reached by a different branch in `read_note` — and it fails too, which is the concrete demonstration that this is not one bug in one function but one *pattern*, repeated wherever a sink was written without the check.

A test that only asserted "the log has content" would pass on this exact fixture and prove nothing, because the vulnerable version logs plenty of content — that is the whole problem. The assertion has to name the specific forbidden string and check for its *absence*, which is a stronger and more specific claim than "logging happened." If you comment out the body of `test_note_body_excluded_from_application_log` and it reports as passed, that is a broken test, not evidence the rule holds — a setup error that skips the check is not proof of anything, and this lesson's lab is deliberately wired so that skipping the check is the only way to make it falsely pass.

## Blast radius: two different failures, not one field twice

The note-body leak and the session-token leak are not the same size of problem wearing two different field names. Reading `tenant-A-secret-body` from a log line tells a reader the content of exactly one note. Reading `sess-alice` from the same line hands that reader a value they can present to the application as if they were its owner — every note that session could read, and, depending on how a write path is built, every note it could modify, becomes reachable, not because of any *further* bug, but because a session token's entire job is to be accepted as proof of identity by everything downstream of it. This is why the lab treats both as separate, independently-checked forbidden outcomes rather than one "sensitive data in logs" bucket: collapsing them would hide that fixing the smaller-blast-radius leak (the body) does nothing at all about the larger one (the token), and a team that stops after the first fix has left the more dangerous failure exactly where it was.

## Why this is the smallest version of the failure, not a simplified one

Three things a real deployment would have that this fixture deliberately omits, and each omission is worth naming rather than glossing over, because a reader should be able to tell "smaller" from "different." There is no real network call, no real TLS termination, and no real multi-process deployment — every request in this lab runs in-process through `fastapi.testclient.TestClient`. Omitting them does not change the cause: the defect is that `log_event` never reads `CLASSIFICATION`, and that fact is true whether the request arrived over a real socket or through a test client calling the same route function directly. There is no real log storage backend — `_LOG_LINES` is a Python list, not a file, a database, or a shipped-to-a-vendor pipeline. Omitting a real backend does not change the cause either: the string that would be written to a real backend is already wrong by the time it reaches `_LOG_LINES.append(...)`, so a real backend downstream of this function would only be a second place the same already-wrong string lands. And there is no cross-company authorization check on the read itself — that is [4.4's](../../../4/4.4/spec.md) property, not this one, and adding it here would not change whether the logged line contains the body or the token; it would only change who is allowed to trigger the request that produces the leak.

## What this lesson is not doing

Do not run this fixture against a production log drain, a real clinic's records, or any live target. Do not paste `tenant-A-secret-body` or `sess-alice` into a ticket, a chat message, or a lesson note "to show someone the bug" — the point of a synthetic fixture value is that it never needs to leave this directory to make the point.
