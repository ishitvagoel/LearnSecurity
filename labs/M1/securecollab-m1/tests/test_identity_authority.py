def test_active_user_can_read_same_company_note(impl) -> None:
    session = impl.login("alice").body["session"]
    assert impl.read_note(session, "n1").status == 200


def test_cross_company_member_is_denied(impl) -> None:
    session = impl.login("bob").body["session"]
    assert impl.read_note(session, "n1").status == 403


def test_client_company_label_cannot_grant_cross_company_read(impl) -> None:
    session = impl.login("bob").body["session"]
    assert impl.read_note(session, "n1", client_company="company-a").status == 403


def test_revoked_user_session_is_denied(impl) -> None:
    session = impl.login("alice").body["session"]
    impl.revoke_user("alice")
    assert impl.read_note(session, "n1").status == 403


def test_logout_revokes_one_session(impl) -> None:
    session = impl.login("alice").body["session"]
    impl.logout(session)
    assert impl.read_note(session, "n1").status == 403
