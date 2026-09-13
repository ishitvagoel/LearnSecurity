from __future__ import annotations

import os
import secrets
import sqlite3
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Response:
    status: int
    body: dict[str, Any]


class SecureCollabM1:
    """Vulnerable local bridge: client labels and stale sessions affect authorization."""

    def __init__(self, database: str | Path | None = None) -> None:
        self.database = str(database or os.environ.get("SECURECOLLAB_DB", ":memory:"))
        self.connection = sqlite3.connect(self.database, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self._lock = threading.Lock()
        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
              id TEXT PRIMARY KEY,
              company TEXT NOT NULL,
              active INTEGER NOT NULL DEFAULT 1
            );
            CREATE TABLE IF NOT EXISTS sessions (
              token TEXT PRIMARY KEY,
              user_id TEXT NOT NULL,
              revoked INTEGER NOT NULL DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS notes (
              id TEXT PRIMARY KEY,
              company TEXT NOT NULL,
              body TEXT NOT NULL
            );
            INSERT OR IGNORE INTO users(id, company, active) VALUES
              ('alice', 'company-a', 1), ('bob', 'company-b', 1);
            INSERT OR IGNORE INTO notes(id, company, body) VALUES
              ('n1', 'company-a', 'Alice synthetic note'),
              ('n2', 'company-b', 'Bob synthetic note');
            """
        )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    def login(self, user_id: str, password: str | None = None) -> Response:
        del password
        token = f"m1-{secrets.token_urlsafe(18)}"
        with self._lock:
            user = self.connection.execute(
                "SELECT id FROM users WHERE id = ? AND active = 1", (user_id,)
            ).fetchone()
            if user is None:
                return Response(403, {"error": "denied"})
            self.connection.execute(
                "INSERT INTO sessions(token, user_id, revoked) VALUES (?, ?, 0)",
                (token, user_id),
            )
            self.connection.commit()
        return Response(200, {"session": token})

    def _session_user(self, session: str) -> sqlite3.Row | None:
        return self.connection.execute(
            "SELECT users.id, users.company FROM sessions JOIN users ON users.id = sessions.user_id WHERE sessions.token = ? AND sessions.revoked = 0",
            (session,),
        ).fetchone()

    def read_note(
        self, session: str, note_id: str, client_company: str | None = None
    ) -> Response:
        with self._lock:
            user = self._session_user(session)
            company = client_company or (user["company"] if user else None)
            note = self.connection.execute(
                "SELECT id, company, body FROM notes WHERE id = ? AND company = ?",
                (note_id, company),
            ).fetchone()
            if user is None or note is None:
                return Response(403, {"error": "denied"})
            return Response(
                200,
                {"id": note["id"], "company": note["company"], "body": note["body"]},
            )

    def revoke_user(self, user_id: str) -> None:
        with self._lock:
            self.connection.execute("UPDATE users SET active = 0 WHERE id = ?", (user_id,))
            self.connection.commit()

    def logout(self, session: str) -> None:
        with self._lock:
            self.connection.execute("UPDATE sessions SET revoked = 1 WHERE token = ?", (session,))
            self.connection.commit()
