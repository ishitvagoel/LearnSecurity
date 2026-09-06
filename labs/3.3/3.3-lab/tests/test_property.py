def test_app_role_cannot_read_other_tenant(impl) -> None:
    assert impl.can_select("app", "tB", "tA") is False


def test_migrator_cannot_select_notes_at_runtime(impl) -> None:
    assert impl.can_select("migrator", "tA", "tA") is False


def test_runtime_connection_is_not_superuser(impl) -> None:
    assert impl.runtime_connection_role() not in {"postgres", "migrator"}


def test_app_role_can_read_own_tenant(impl) -> None:
    assert impl.can_select("app", "tA", "tA") is True
