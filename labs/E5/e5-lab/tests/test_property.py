def test_body_cannot_switch_tenant(impl):
    assert impl.tenant_for({"tenant": "A"}, {"tenant": "B"}) == "A"


def test_matching_body_may_keep_session_tenant(impl):
    assert impl.tenant_for({"tenant": "A"}, {"tenant": "A"}) == "A"
