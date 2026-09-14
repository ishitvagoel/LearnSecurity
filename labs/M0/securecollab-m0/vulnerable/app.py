from __future__ import annotations

import os
import sqlite3
import threading
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ACTORS = {"alice": "company-a", "bob": "company-b"}


@dataclass(frozen=True)
class Response:
    status: int
    body: dict[str, Any]


class SecureCollabM0:
    """Vulnerable local fixture: client company input controls the database lookup."""

    def __init__(self, database: str | Path | None = None) -> None:
        self.connection = sqlite3.connect(str(database or os.environ.get("SECURECOLLAB_DB", ":memory:")), check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self._lock = threading.Lock()
        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS notes (
              id TEXT PRIMARY KEY,
              company TEXT NOT NULL,
              body TEXT NOT NULL
            );
            INSERT OR IGNORE INTO notes(id, company, body)
              VALUES ('n1', 'company-a', 'Alice synthetic note');
            """
        )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    def read_note(self, actor_id: str, note_id: str, client_company: str | None = None) -> Response:
        company = client_company or ACTORS.get(actor_id)
        with self._lock:
            row = self.connection.execute(
                "SELECT id, company, body FROM notes WHERE id = ? AND company = ?", (note_id, company)
            ).fetchone()
        if row is None:
            return Response(403, {"error": "denied"})
        return Response(200, {"id": row["id"], "company": row["company"], "body": row["body"]})
