"""SecureCollab's Phase 3 asset-classification sink (VULNERABLE), as a local fixture.

A FastAPI service exposes one asset (a note body) and one authority artifact
(a session token) through two independent sinks: an application log
(`log_event`) and an error/diagnostic dump (`write_error_dump`) that an
exception handler writes to when a lookup fails. `SECURITY.md` names the
forbidden outcomes; do not "fix" this file in place -- see `fixed/app.py`
for the structural repair and `../README.md` for how to run both.

The defect is not "nobody classified the data." `CLASSIFICATION` below is a
real table, with real levels, that a reviewer could point to in a design
document. The defect is that neither sink ever reads it. A label that does
not change what a sink accepts is a label, not a control -- this fixture
exists to make that distinction checkable rather than asserted.

Two independent sinks share the same shape of failure:

1. `log_event` (C1, C2): pastes every field of the context dictionary it is
   given into the log line, including `note_body` (classified confidential)
   and `session_token` (an authority artifact, also confidential, and a
   strictly worse leak than the body -- see `lessons/01-property.md`).

2. `write_error_dump` (C2, C5): a *different* piece of code, reached only
   when a note lookup fails, that dumps the same kind of raw context. Fixing
   the logger does not touch this function; a second, independent place the
   same fields can leak from is exactly why a per-sink rule, not a per-field
   promise, is the property (`02-model.md`).

There is no `CLASSIFICATION`-driven allow-list anywhere in this file. A field
this fixture has never named at all (see the `X-Debug-Hint` header in the
tests) leaks exactly as readily as `note_body` does, because nothing here
treats an unrecognized field as anything other than "print it" -- the
opposite of the fail-safe default `fixed/app.py` restores.
"""

from __future__ import annotations

from fastapi import FastAPI, Header, HTTPException

# The classification "spreadsheet." It is accurate, it is reviewed, and it
# is never consulted by either sink below -- that gap is the entire lesson.
CLASSIFICATION: dict[str, str] = {
    "note_body": "confidential",
    "session_token": "confidential",
    "note_id": "internal",
    "company_id": "internal",
    "event": "internal",
}

SESSIONS: dict[str, str] = {
    "sess-alice": "companyA",
    "sess-bob": "companyB",
}

NOTES: dict[str, dict[str, str]] = {}
_LOG_LINES: list[str] = []
_ERROR_DUMPS: list[dict] = []


def reset() -> None:
    """Called by the test fixture before every test; no state persists
    between mental experiments."""
    NOTES.clear()
    NOTES["n1"] = {"company_id": "companyA", "note_body": "tenant-A-secret-body"}
    _LOG_LINES.clear()
    _ERROR_DUMPS.clear()


def log_event(event: str, context: dict) -> None:
    """VULNERABLE: every field of `context` is pasted into the line,
    verbatim, regardless of what `CLASSIFICATION` says about it."""
    rendered = " ".join(f"{key}={value}" for key, value in context.items())
    _LOG_LINES.append(f"{event}: {rendered}")


def write_error_dump(context: dict) -> None:
    """VULNERABLE: a second sink, reached only on failure, that dumps the
    same unredacted context an exception handler was "just trying to help
    debug" with."""
    _ERROR_DUMPS.append(dict(context))


def _bearer(authorization: str | None) -> str | None:
    if not authorization or not authorization.startswith("Bearer "):
        return None
    return authorization[len("Bearer "):]


def create_app() -> FastAPI:
    app = FastAPI()

    @app.put("/notes/{note_id}")
    def put_note(
        note_id: str,
        payload: dict,
        authorization: str | None = Header(default=None),
    ) -> dict:
        token = _bearer(authorization)
        company = SESSIONS.get(token) if token else None
        if company is None:
            raise HTTPException(status_code=401, detail="unknown session")
        NOTES[note_id] = {"company_id": company, "note_body": str(payload.get("body", ""))}
        return {"stored": True}

    @app.post("/notes/{note_id}/read")
    def read_note(
        note_id: str,
        authorization: str | None = Header(default=None),
        x_debug_hint: str | None = Header(default=None, alias="X-Debug-Hint"),
    ) -> dict:
        token = _bearer(authorization)
        company = SESSIONS.get(token) if token else None
        if company is None:
            raise HTTPException(status_code=401, detail="unknown session")

        note = NOTES.get(note_id)
        if note is None:
            context = {
                "event": "note_read_error",
                "note_id": note_id,
                "company_id": company,
                "session_token": token,
            }
            if x_debug_hint:
                context["debug_hint"] = x_debug_hint
            write_error_dump(context)
            raise HTTPException(status_code=404, detail="not found")

        context = {
            "event": "note_read",
            "note_id": note_id,
            "company_id": company,
            "note_body": note["note_body"],
            "session_token": token,
        }
        if x_debug_hint:
            context["debug_hint"] = x_debug_hint
        log_event("note_read", context)
        return {"note_id": note_id, "logged": True}

    @app.get("/internal/log-lines")
    def log_lines() -> dict:
        return {"lines": list(_LOG_LINES)}

    @app.get("/internal/error-dumps")
    def error_dumps() -> dict:
        return {"dumps": list(_ERROR_DUMPS)}

    return app
