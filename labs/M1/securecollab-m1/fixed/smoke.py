from __future__ import annotations

from app import SecureCollabM1


def main() -> None:
    app = SecureCollabM1()
    try:
        alice = app.login("alice", "alice-local-password").body["session"]
        bob = app.login("bob", "bob-local-password").body["session"]
        assert app.read_note(alice, "n1").status == 200
        assert app.read_note(bob, "n1").status == 403
        assert app.read_note(bob, "n1", client_company="company-a").status == 403
        app.revoke_user("alice")
        assert app.read_note(alice, "n1").status == 403
    finally:
        app.close()
    print("M1 fixed smoke: PASS")


if __name__ == "__main__":
    main()
