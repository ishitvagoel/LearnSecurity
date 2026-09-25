"""Fixed: the idempotency key is enforced by the store, not by application
logic that checks and then acts in two separate steps.

A tempting "fix" is: SELECT to see whether the key exists, and if not, then
INSERT. That reads correctly in a single-threaded trace and is exactly the
shape that fails under real concurrency -- two requests can both run the
SELECT and both see "not found" before either has run the INSERT, because
the check and the act are not one atomic operation (see 03-break.md and the
test_concurrent_* case below). This file does not do that. `idempotency_key`
carries a UNIQUE constraint at the schema level, so the database itself
rejects a second row with the same key no matter how the two requests are
interleaved in time -- the atomicity comes from the storage engine's own
write-serialization, not from application-level timing. Two NULLs (a request
with no key at all) are not equal under SQL UNIQUE, matching this fixture's
declared leftover: a missing key still shares once per call.
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
    global _db_path
    fd, raw_path = tempfile.mkstemp(suffix=".db", prefix="lab24-fixed-")
    Path(raw_path).unlink()
    _db_path = Path(raw_path)
    conn = _connect()
    conn.execute(
        "CREATE TABLE shares ("
        "  id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "  note_id TEXT NOT NULL,"
        "  idempotency_key TEXT UNIQUE"
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
    try:
        conn = _connect()
    except sqlite3.Error:
        # The store is unreachable. Deny the action rather than accept it
        # "just this once" -- fail-closed for a high-impact write, per
        # ASVS v5.0.0-16.5.3 and this module's Operate lesson.
        return {"accepted": False, "reason": "store_unavailable"}

    try:
        if idempotency_key:
            try:
                conn.execute(
                    "INSERT INTO shares (note_id, idempotency_key) VALUES (?, ?)",
                    (note_id, idempotency_key),
                )
                conn.commit()
                share_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
                return {"accepted": True, "share_id": share_id, "replayed": False}
            except sqlite3.IntegrityError:
                # The UNIQUE constraint just did the check-and-act
                # atomically on our behalf: some row, possibly written by a
                # request that raced this one, already holds this key.
                # Return that row's outcome rather than a second one.
                conn.rollback()
                row = conn.execute(
                    "SELECT id FROM shares WHERE idempotency_key = ?",
                    (idempotency_key,),
                ).fetchone()
                return {"accepted": True, "share_id": row[0], "replayed": True}
        else:
            conn.execute(
                "INSERT INTO shares (note_id, idempotency_key) VALUES (?, NULL)",
                (note_id,),
            )
            conn.commit()
            share_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
            return {"accepted": True, "share_id": share_id, "replayed": False}
    finally:
        conn.close()
