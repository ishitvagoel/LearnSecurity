"""SecureCollab's Phase 3 asset-classification sink (FIXED), as a local fixture.

Same two sinks as `vulnerable/app.py` -- an application log and an
error/diagnostic dump -- but both now route every field through `_redact`,
which consults `CLASSIFICATION` and a per-sink `SINK_POLICY` before a value
is allowed to reach the rendered line. See `../README.md` for the invariant
and how to run both variants, and `SECURITY.md` for what this file changes.

Three properties this file restores, each named in
`content/modules/3/3.1/spec.md`'s teaching claims:

1. **A sink rule, not a label (C1).** `CLASSIFICATION` is the same table
   `vulnerable/app.py` carried and never used. Here, `_redact` reads it
   before either sink accepts a field, so the label actually changes what
   the sink emits.

2. **An authority artifact is classified at least as sensitively as the
   content it gates (C2).** `session_token` carries the same `confidential`
   level as `note_body`, and both sinks deny it identically -- a session
   token reaching either sink lets whoever reads that sink act as the
   token's owner, not merely read one field's content.

3. **An unclassified field defaults to the most restrictive level, not the
   least (C4).** `_redact`'s `CLASSIFICATION.get(key, "confidential")` means
   a field this table has never named -- the next schema addition nobody
   has classified yet -- is denied by every sink until someone positively
   assigns it a level. Silence is not "public"; silence is "confidential
   until decided," which is the only default a fail-safe rule can have.

What this file does **not** claim to fix: an exception middleware or slow
query log elsewhere in a real deployment that never calls `write_error_dump`
at all bypasses this mechanism entirely, because a per-sink rule only
governs the sinks it was written into. That residual is named in
`lessons/01-property.md` and `lessons/06-operate.md`, not hidden here.
"""

from __future__ import annotations

from fastapi import FastAPI, Header, HTTPException

CLASSIFICATION: dict[str, str] = {
    "note_body": "confidential",
    "session_token": "confidential",
    "note_id": "internal",
    "company_id": "internal",
    "event": "internal",
}

# The documented protection requirement per sink (ASVS v5.0.0-14.1.2): which
# levels each sink is allowed, by design, to carry. Neither sink here has a
# documented operational need for a confidential field, so neither allows
# one -- redaction is not "whatever the code author remembered to strip,"
# it is "whatever this sink's own documented policy admits."
SINK_POLICY: dict[str, set[str]] = {
    "application_log": {"internal"},
    "error_dump": {"internal"},
}

SESSIONS: dict[str, str] = {
    "sess-alice": "companyA",
    "sess-bob": "companyB",
}

NOTES: dict[str, dict[str, str]] = {}
_LOG_LINES: list[str] = []
_ERROR_DUMPS: list[dict] = []


def reset() -> None:
    NOTES.clear()
    NOTES["n1"] = {"company_id": "companyA", "note_body": "tenant-A-secret-body"}
    _LOG_LINES.clear()
    _ERROR_DUMPS.clear()


def _redact(context: dict, sink: str) -> dict:
    """Fail-safe default: `CLASSIFICATION.get(key, "confidential")` means a
    key this table was never told about is treated as the MOST sensitive
    level that exists, not the least. An unclassified field is not a field
    with no risk; it is a field whose risk nobody has looked at yet, and
    every sink here treats "nobody looked at it yet" as "deny."

    The value is not simply dropped -- it is replaced with a marker that
    still names the level that blocked it, so an operator reading the log
    can see that a field existed and was withheld, rather than seeing
    nothing and wondering whether the field was ever populated at all.
    """
    allowed_levels = SINK_POLICY[sink]
    out: dict = {}
    for key, value in context.items():
        level = CLASSIFICATION.get(key, "confidential")
        out[key] = value if level in allowed_levels else f"[redacted-{level}]"
    return out


def log_event(event: str, context: dict) -> None:
    safe = _redact(context, "application_log")
    rendered = " ".join(f"{key}={value}" for key, value in safe.items())
    _LOG_LINES.append(f"{event}: {rendered}")


def write_error_dump(context: dict) -> None:
    _ERROR_DUMPS.append(_redact(context, "error_dump"))


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
