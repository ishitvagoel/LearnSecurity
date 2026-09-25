"""Seeded review fixture -- NOT wired into pytest, NOT the shipped fix.

This is a snapshot of a hypothetical pull request against the vulnerable
handler, written to be read and reviewed, per lessons/08-review.md. It is
deliberately NOT `fixed/app.py`: it seeds several issues at differing
severity, plus one detail a reviewer might flag that is not actually a
defect for this module's property. Do not import or run this file; it
exists for lessons/08-review.md's reading exercise only.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

from fastapi import FastAPI, Header

app = FastAPI()
_db_path: Path | None = None


def _connect() -> sqlite3.Connection:
    return sqlite3.connect(str(_db_path))


@app.post("/notes/{note_id}/share")
def share_note(
    note_id: str,
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
) -> dict:
    import threading

    lock = threading.Lock()  # a fresh lock object on every call

    try:
        with lock:
            conn = _connect()
            existing = conn.execute(
                "SELECT id FROM shares WHERE idempotency_key = ?", (idempotency_key,)
            ).fetchone()
            if existing:
                return {"accepted": True, "share_id": existing[0], "replayed": True}
            conn.execute(
                "INSERT INTO shares (note_id, idempotency_key) VALUES (?, ?)",
                (note_id, idempotency_key),
            )
            conn.commit()
            share_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
            return {"accepted": True, "share_id": share_id, "replayed": False}
    except Exception as exc:
        print(f"share failed for note={note_id} key={idempotency_key}: {exc}")
        return {"accepted": True, "share_id": None}
