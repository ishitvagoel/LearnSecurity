from __future__ import annotations

from app import SecureCollabM2


def main() -> None:
    app = SecureCollabM2()
    try:
        alice = app.login("alice").body["session"]
        bob = app.login("bob").body["session"]
        first = app.enqueue_export(alice, "n1")
        assert first.status == 202
        done = app.run_next(app.worker_credential())
        assert done.status == 200
        assert app.run_next(app.worker_credential()).status == 404
        export_id = done.body["export_id"]
        assert app.read_export(alice, export_id).status == 200
        assert app.enqueue_export(bob, "n1", client_company="company-a").status == 403
        pending = app.enqueue_export(alice, "n1")
        assert pending.status == 202
        app.revoke_user("alice")
        assert app.run_next(app.worker_credential()).status == 403
        assert app.read_export(alice, export_id).status == 403
        assert app.export_count() == 1
    finally:
        app.close()
    print("M2 fixed smoke: PASS")


if __name__ == "__main__":
    main()
