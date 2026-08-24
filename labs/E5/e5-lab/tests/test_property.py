def test_body_cannot_switch_tenant(impl):
    assert impl.tenant_for({'tenant': 'A'}, {'tenant': 'B'}) == 'A'
