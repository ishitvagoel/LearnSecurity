def test_member_cannot_resolve_internal_field(impl):
    assert impl.resolve('member','secret_internal') is False
