from __future__ import annotations

import os
import hashlib
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


DEMO_PASSWORDS = {"alice": "alice-local-password", "bob": "bob-local-password"}


def _password_verifier(user_id: str, password: str) -> str:
    salt = f"securecollab-m1:{user_id}".encode("utf-8")
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 120_000)
    return f"{salt.hex()}:{digest.hex()}"


class SecureCollabM1:
    """Local M1 bridge with server-side sessions and object-level authorization."""

    def __init__(self, database: str | Path | None = None) -> None:
        self.database = str(database or os.environ.get("SECURECOLLAB_DB", ":memory:"))
        self.connection = sqlite3.connect(self.database, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self._lock = threading.Lock()
        # Keep a learner's existing local fixture usable after upgrading from
        # the pre-credential bridge. Production migrations belong in the
        # application stack; this small bridge only needs this additive step.
        user_columns = {row[1] for row in self.connection.execute("PRAGMA table_info(users)")}
        if user_columns and "password_hash" not in user_columns:
            self.connection.execute("ALTER TABLE users ADD COLUMN password_hash TEXT NOT NULL DEFAULT ''")
        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
              id TEXT PRIMARY KEY,
              company TEXT NOT NULL,
              active INTEGER NOT NULL DEFAULT 1,
              password_hash TEXT NOT NULL DEFAULT ''
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
            INSERT OR IGNORE INTO users(id, company, active, password_hash) VALUES
              ('alice', 'company-a', 1, ''), ('bob', 'company-b', 1, '');
            INSERT OR IGNORE INTO notes(id, company, body) VALUES
              ('n1', 'company-a', 'Alice synthetic note'),
              ('n2', 'company-b', 'Bob synthetic note');
            """
        )
        for user_id, password in DEMO_PASSWORDS.items():
            self.connection.execute(
                "UPDATE users SET password_hash = ? WHERE id = ? AND password_hash = ''",
                (_password_verifier(user_id, password), user_id),
            )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    def login(self, user_id: str, password: str | None = None) -> Response:
        token = f"m1-{secrets.token_urlsafe(18)}"
        with self._lock:
            user = self.connection.execute(
                "SELECT id, password_hash FROM users WHERE id = ? AND active = 1", (user_id,)
            ).fetchone()
            if user is None or password is None:
                return Response(403, {"error": "denied"})
            expected = _password_verifier(user_id, password)
            if not secrets.compare_digest(str(user["password_hash"]), expected):
                return Response(403, {"error": "denied"})
            self.connection.execute(
                "INSERT INTO sessions(token, user_id, revoked) VALUES (?, ?, 0)",
                (token, user_id),
            )
            self.connection.commit()
        return Response(200, {"session": token})

    def _current_user(self, session: str) -> sqlite3.Row | None:
        return self.connection.execute(
            """
            SELECT users.id, users.company
            FROM sessions JOIN users ON users.id = sessions.user_id
            WHERE sessions.token = ? AND sessions.revoked = 0 AND users.active = 1
            """,
            (session,),
        ).fetchone()

    def read_note(
        self, session: str, note_id: str, client_company: str | None = None
    ) -> Response:
        del client_company
        with self._lock:
            user = self._current_user(session)
            note = self.connection.execute(
                "SELECT id, company, body FROM notes WHERE id = ?", (note_id,)
            ).fetchone()
            if user is None or note is None or note["company"] != user["company"]:
                return Response(403, {"error": "denied"})
            return Response(
                200,
                {"id": note["id"], "company": note["company"], "body": note["body"]},
            )

    def revoke_user(self, user_id: str) -> None:
        with self._lock:
            self.connection.execute("UPDATE users SET active = 0 WHERE id = ?", (user_id,))
            self.connection.execute("UPDATE sessions SET revoked = 1 WHERE user_id = ?", (user_id,))
            self.connection.commit()

    def logout(self, session: str) -> None:
        with self._lock:
            self.connection.execute("UPDATE sessions SET revoked = 1 WHERE token = ?", (session,))
            self.connection.commit()
