def test_allowed_export_is_written(impl) -> None:
    session = impl.login("alice").body["session"]
    assert impl.enqueue_export(session, "n1").status == 202
    assert impl.run_next().status == 200
    assert impl.export_count() == 1


def test_forged_tenant_cannot_enqueue_foreign_note(impl) -> None:
    session = impl.login("bob").body["session"]
    assert impl.enqueue_export(session, "n1", client_company="company-a").status == 403


def test_revocation_before_worker_run_denies_and_writes_no_copy(impl) -> None:
    session = impl.login("alice").body["session"]
    assert impl.enqueue_export(session, "n1").status == 202
    impl.revoke_user("alice")
    assert impl.run_next().status == 403
    assert impl.export_count() == 0


def test_revoked_session_cannot_read_retained_export(impl) -> None:
    session = impl.login("alice").body["session"]
    assert impl.enqueue_export(session, "n1").status == 202
    done = impl.run_next()
    assert done.status == 200
    impl.revoke_user("alice")
    assert impl.read_export(session, done.body["export_id"]).status == 403
