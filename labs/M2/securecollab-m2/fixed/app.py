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


class SecureCollabM2:
    """Local M2 bridge with current authority checks at enqueue and worker time."""

    def __init__(self, database: str | Path | None = None) -> None:
        self.database = str(database or os.environ.get("SECURECOLLAB_DB", ":memory:"))
        self.connection = sqlite3.connect(self.database, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self._lock = threading.Lock()
        # Local stand-in for a workload identity issued by the runtime. The
        # credential is never copied into a queued message.
        self._worker_credential = secrets.token_urlsafe(24)
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
            CREATE TABLE IF NOT EXISTS jobs (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              actor_id TEXT NOT NULL,
              note_id TEXT NOT NULL,
              status TEXT NOT NULL,
              export_id INTEGER
            );
            CREATE TABLE IF NOT EXISTS exports (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              job_id INTEGER NOT NULL,
              actor_id TEXT NOT NULL,
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

    def worker_credential(self) -> str:
        """Return the synthetic credential used by this local worker."""
        return self._worker_credential

    def login(self, user_id: str) -> Response:
        token = f"m2-{secrets.token_urlsafe(18)}"
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

    def _current_user(self, session: str) -> sqlite3.Row | None:
        return self.connection.execute(
            """
            SELECT users.id, users.company
            FROM sessions JOIN users ON users.id = sessions.user_id
            WHERE sessions.token = ? AND sessions.revoked = 0 AND users.active = 1
            """,
            (session,),
        ).fetchone()

    def enqueue_export(
        self, session: str, note_id: str, client_company: str | None = None
    ) -> Response:
        del client_company
        with self._lock:
            user = self._current_user(session)
            note = self.connection.execute(
                "SELECT id, company FROM notes WHERE id = ?", (note_id,)
            ).fetchone()
            if user is None or note is None or note["company"] != user["company"]:
                return Response(403, {"error": "denied"})
            job = self.connection.execute(
                "INSERT INTO jobs(actor_id, note_id, status) VALUES (?, ?, 'queued')",
                (user["id"], note["id"]),
            )
            self.connection.commit()
            return Response(202, {"job_id": int(job.lastrowid)})

    def revoke_user(self, user_id: str) -> None:
        with self._lock:
            self.connection.execute("UPDATE users SET active = 0 WHERE id = ?", (user_id,))
            self.connection.execute("UPDATE sessions SET revoked = 1 WHERE user_id = ?", (user_id,))
            self.connection.commit()

    def run_next(self, worker_credential: str | None = None) -> Response:
        with self._lock:
            job = self.connection.execute(
                "SELECT id, actor_id, note_id FROM jobs WHERE status = 'queued' ORDER BY id LIMIT 1"
            ).fetchone()
            if job is None:
                return Response(404, {"error": "no-job"})
            supplied = worker_credential or ""
            if not secrets.compare_digest(supplied, self._worker_credential):
                self.connection.execute("UPDATE jobs SET status = 'denied' WHERE id = ?", (job["id"],))
                self.connection.commit()
                return Response(403, {"error": "denied"})
            actor = self.connection.execute(
                "SELECT id, company FROM users WHERE id = ? AND active = 1", (job["actor_id"],)
            ).fetchone()
            note = self.connection.execute(
                "SELECT id, company, body FROM notes WHERE id = ?", (job["note_id"],)
            ).fetchone()
            if actor is None or note is None or actor["company"] != note["company"]:
                self.connection.execute("UPDATE jobs SET status = 'denied' WHERE id = ?", (job["id"],))
                self.connection.commit()
                return Response(403, {"error": "denied"})
            export = self.connection.execute(
                "INSERT INTO exports(job_id, actor_id, company, body) VALUES (?, ?, ?, ?)",
                (job["id"], actor["id"], actor["company"], note["body"]),
            )
            self.connection.execute(
                "UPDATE jobs SET status = 'complete', export_id = ? WHERE id = ?",
                (export.lastrowid, job["id"]),
            )
            self.connection.commit()
            return Response(200, {"job_id": job["id"], "export_id": int(export.lastrowid)})

    def read_export(self, session: str, export_id: int) -> Response:
        with self._lock:
            user = self._current_user(session)
            export = self.connection.execute(
                "SELECT id, company, body FROM exports WHERE id = ?", (export_id,)
            ).fetchone()
            if user is None or export is None or export["company"] != user["company"]:
                return Response(403, {"error": "denied"})
            return Response(200, {"id": export["id"], "company": export["company"], "body": export["body"]})

    def export_count(self) -> int:
        with self._lock:
            row = self.connection.execute("SELECT COUNT(*) AS count FROM exports").fetchone()
            return int(row["count"])
