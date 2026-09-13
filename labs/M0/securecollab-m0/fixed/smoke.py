try:
    from .app import SecureCollabM0
except ImportError:  # Support the documented `python fixed/smoke.py` form.
    from app import SecureCollabM0

app = SecureCollabM0()
try:
    assert app.read_note("alice", "n1").status == 200
    assert app.read_note("bob", "n1").status == 403
    assert app.read_note("bob", "n1", client_company="company-a").status == 403
    print("M0 fixed smoke: PASS")
finally:
    app.close()
