def test_deeplink_as_param_does_not_switch_user(impl):
    impl.open_link({"as": "admin"})
    assert impl.current_user() == "alice"


def test_note_deep_link_keeps_session(impl):
    impl.open_link({"note": "n1"})
    assert impl.current_user() == "alice"
