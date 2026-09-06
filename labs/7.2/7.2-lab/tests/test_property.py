def test_member_cannot_resolve_internal_field(impl):
    assert impl.resolve("member", "secret_internal") is False


def test_member_can_resolve_display_name(impl):
    assert impl.resolve("member", "display_name") is True


def test_service_can_resolve_internal_field(impl):
    assert impl.resolve("service", "secret_internal") is True
