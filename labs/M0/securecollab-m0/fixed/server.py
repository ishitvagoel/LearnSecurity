from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from app import SecureCollabM0

ROOT = Path(__file__).resolve().parents[1]
APP = SecureCollabM0()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - stdlib HTTP API name
        parsed = urlparse(self.path)
        if parsed.path == "/":
            body = (ROOT / "browser" / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if parsed.path.startswith("/notes/"):
            note_id = parsed.path.removeprefix("/notes/")
            actor = self.headers.get("X-Demo-Actor", "")
            client_company = parse_qs(parsed.query).get("company", [None])[0]
            response = APP.read_note(actor, note_id, client_company)
            body = APP.as_json(response)
            self.send_response(response.status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self.send_error(404)

    def log_message(self, format: str, *args: object) -> None:
        return


if __name__ == "__main__":
    print("SecureCollab M0 fixed fixture: http://127.0.0.1:8765/")
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
