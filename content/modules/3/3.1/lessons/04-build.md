# Redact at the sink: a default-deny allow-list, not a field-name patch

**Kind:** design-exercise
**Loop step:** 4 Build

## Predicting the fix before reading it

[`lessons/03-break.md`](03-break.md) located the defect at one line: `log_event` renders every field of `context` with nothing checking classification against sink policy first. Given that diagnosis, the shape of the fix should already be predictable without reading `fixed/app.py` at all: something has to sit between "the fields the caller built" and "the string that gets rendered," consult both the field's classification level and the sink's own permitted levels, and decide per field, not per call. Whatever else the fix does, it has to run *inside* the sink function — or in something every sink function unconditionally calls before rendering — because [`lessons/01-property.md`](01-property.md) already established that a classification table sitting nearby, unread, is not a control regardless of how accurate it is.

## Two candidates, and where the weaker one breaks

**Candidate A: filter by field name at each call site.** Wherever a handler builds a context dictionary destined for a sink, have that handler itself strip `note_body` and `session_token` before calling `log_event`. A competent engineer under time pressure would reasonably propose this — it requires no change to `log_event` at all, and it can be shipped by editing only the handler that currently has the bug. It fails for a reason [`lessons/02-model.md`](02-model.md) already previewed: it is a fix scoped to *this* handler, not to the sink. The moment a second handler builds its own context dictionary for the same sink — a different endpoint, a different exception path, a feature added six months from now by an engineer who has never read this handler's code — that new call site starts from zero, with no strip-list of its own, and the leak reappears at a different address. Candidate A fixes an instance of the failure. It does not fix the sink.

**Candidate B: an allow-list inside the sink, keyed by classification level, defaulting to deny.** Instead of trusting every caller of `log_event` to remember which fields to strip, make `log_event` itself refuse to render any field whose level is not in that sink's documented policy — and, critically, treat a field the classification table has never named as the *most* restrictive level rather than the least. This is `fixed/app.py`'s actual design:

```python
def _redact(context: dict, sink: str) -> dict:
    allowed_levels = SINK_POLICY[sink]
    out: dict = {}
    for key, value in context.items():
        level = CLASSIFICATION.get(key, "confidential")
        out[key] = value if level in allowed_levels else f"[redacted-{level}]"
    return out
```

`CLASSIFICATION.get(key, "confidential")` is the one line worth pausing on longest in this entire file. `.get(key, "confidential")` means: if this table has never heard of `key`, treat it as `"confidential"` — the same level assigned to the note body and the session token, not the level assigned to `note_id` or `event`. Contrast this with the far more natural-looking `.get(key, "internal")` or even `.get(key)` returning `None` and being silently allowed through by a buggy comparison — either of those defaults an *unknown* field toward *permissive*, which reproduces exactly the failure this module exists to prevent, just one level removed: instead of "every field leaks because nothing checks," it becomes "every field this table's author forgot to list leaks because the default assumed it was safe." A fail-safe default has to fail toward the restrictive side, every time, or it is not actually fail-safe — it is just a smaller allow-list with the same shape of gap.

Candidate B still needs one thing candidate A did not: every handler that reaches a sink has to actually call `log_event` or `write_error_dump` rather than writing to `_LOG_LINES` or a real logging backend directly. That is not a weakness unique to candidate B — it is the boundary this entire mechanism assumes, named honestly rather than hidden, in the next section.

## Where this mechanism itself stops working

A per-sink allow-list only governs the sinks it is wired into. If a future feature adds a third sink — an audit export, say — and that export's code builds its own string directly from a note object instead of calling through `log_event` or `write_error_dump`, `_redact` never runs, and the export leaks exactly as the original bug did, because this fix protects two named functions, not "every place a string can end up in this codebase." Exception middleware, a slow-query logger, or a full-request-capture APM agent that FastAPI or a hosting platform installs beneath the application's own code are the concrete version of this limit: none of them call `log_event`, so none of them are touched by this fix at all. Naming this limit here is not a hedge; it is the honest boundary of what a sink-level check can promise, and it is why [`lessons/06-operate.md`](06-operate.md) pairs this fix with a detection signal rather than presenting the fix alone as sufficient.

## Framework default versus application guarantee, with a concrete gap between them

FastAPI, and Python's standard logging module beneath most real deployments, will format whatever you hand them — a dictionary, an f-string, an object's `__repr__` — with no concept of "confidential" at all. This is not a criticism of the framework; a general-purpose logging library cannot know your application's classification scheme, and it would be actively worse if it silently applied one guess at every deployment's discretion. The concrete gap this creates: a framework's exception handler, invoked automatically when an unhandled error occurs, commonly formats the entire request object — headers, body, query parameters — into whatever error page or log entry it produces by default, because "show everything, so a developer can debug it" is a reasonable *default* for a framework that has no way to know which of your fields are Confidential. `write_error_dump` in this lab's fixture is a deliberately simplified stand-in for that exact behavior: a real deployment's default exception handler is this lesson's `write_error_dump`, before anyone has added the check `fixed/app.py` shows. The requirement — deny by classification, default to the most restrictive level — is the application's to build and to own; it is not a setting a framework ships pre-configured, because the framework was never told what your fields mean.

## Practice

Add a third sink to the fixed fixture in your own head, without writing code: a hypothetical `write_audit_export(context)` that a future feature might add. Using `_redact`'s existing signature, write the one line that export function would need to call to inherit this lesson's guarantee, and name the one thing that would still need deciding before that line could ship — the export sink's own `SINK_POLICY` entry, since an export may legitimately need to carry fields neither the log nor the error dump are documented to carry.

## What can still go wrong

A hand-written allow-list is only as correct as the humans who maintain `CLASSIFICATION` and `SINK_POLICY`; nothing in this mechanism catches a level that was assigned wrong in the first place. Regex-based redaction applied *after* a string is already rendered — as opposed to this lesson's field-level check applied *before* rendering — can miss an encoded, escaped, or re-serialized copy of a denied value, which is why `fixed/app.py` denies at the field, not by scanning the finished line for a pattern.
