"""Vulnerable: share_note inserts on every call and never fails closed.

This is a real FastAPI component, not a two-line predicate: a request cycle
(POST /notes/{note_id}/share) drives a persistent SQLite store the same way a
retrying browser, a load balancer, or a redelivering worker would. Two
defects live here, both variants of the same root cause -- the handler never
asks "have I already committed this exact idempotency key?" before it acts:

1. No idempotency check at all. Every POST is a fresh INSERT, so a retry
   after a timeout, a double-click, or two workers delivering the same job
   duplicates the share.
2. No fail-closed path. If the store cannot be reached, the handler still
   reports success rather than denying the action -- optimism, not a check.
"""
from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

from fastapi import FastAPI, Header

app = FastAPI()

_db_path: Path | None = None


def _connect() -> sqlite3.Connection:
    assert _db_path is not None, "call reset() before using this fixture"
    return sqlite3.connect(str(_db_path), timeout=5.0)


def reset() -> None:
    """Fresh on-disk SQLite file per test, matching the other labs'
    reset()-between-tests convention. Not in-memory: a real file is what
    lets independent connections from independent threads see the same
    committed rows, which the concurrency test below depends on."""
    global _db_path
    fd, raw_path = tempfile.mkstemp(suffix=".db", prefix="lab24-vuln-")
    Path(raw_path).unlink()
    _db_path = Path(raw_path)
    conn = _connect()
    conn.execute(
        "CREATE TABLE shares ("
        "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "  note_id TEXT NOT NULL,"
        "  idempotency_key TEXT"
        ")"
    )
    conn.commit()
    conn.close()


def share_count() -> int:
    conn = _connect()
    try:
        return conn.execute("SELECT COUNT(*) FROM shares").fetchone()[0]
    finally:
        conn.close()


@app.post("/notes/{note_id}/share")
def share_note(
    note_id: str,
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
) -> dict:
    # Fail-open by construction: any storage problem is swallowed and the
    # caller is told it worked anyway. This is the module's second forbidden
    # outcome -- "the key store is slow or down" must never be read as
    # permission to proceed "just this once".
    try:
        conn = _connect()
        conn.execute(
            "INSERT INTO shares (note_id, idempotency_key) VALUES (?, ?)",
            (note_id, idempotency_key),
        )
        conn.commit()
        share_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        conn.close()
        return {"accepted": True, "share_id": share_id}
    except sqlite3.Error:
        return {"accepted": True, "share_id": None}
