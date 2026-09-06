def test_honest_grant_on_n1_allows_read(impl) -> None:
    assert impl.can_read("bob", "n1") is True


def test_owner_reads_own_note(impl) -> None:
    assert impl.can_read("alice", "n2") is True


def test_grant_on_n1_is_not_grant_on_n2(impl) -> None:
    assert impl.can_read("bob", "n2") is False


def test_cross_tenant_owner_is_denied(impl) -> None:
    assert impl.can_read("alice", "n3") is False


def test_admin_role_is_not_cross_tenant(impl) -> None:
    assert impl.can_read("eve", "n1") is False


def test_tenant_admin_role_is_not_object_grant(impl) -> None:
    assert impl.can_read("eve", "n3") is False
