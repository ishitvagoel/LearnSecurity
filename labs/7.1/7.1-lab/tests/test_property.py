def test_is_admin_cannot_be_patched(impl):
    u = {"display_name": "a", "is_admin": False}
    out = impl.apply(u, {"is_admin": True})
    assert out["is_admin"] is False


def test_display_name_can_be_patched(impl):
    u = {"display_name": "a", "is_admin": False}
    out = impl.apply(u, {"display_name": "b"})
    assert out["display_name"] == "b"
    assert out["is_admin"] is False


def test_unknown_key_does_not_appear(impl):
    u = {"display_name": "a", "is_admin": False}
    out = impl.apply(u, {"role": "admin"})
    assert "role" not in out
    assert out["is_admin"] is False
