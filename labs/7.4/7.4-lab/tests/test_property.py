def test_user_session_is_not_worker_identity(impl):
    assert impl.exporter({"user_session": "alice", "service": None}) is None


def test_service_principal_is_worker_identity(impl):
    assert impl.exporter({"service": "worker-sc"}) == "worker-sc"


def test_alice_and_wrong_service_is_rejected(impl):
    assert impl.exporter({"user_session": "alice", "service": "not-worker"}) is None
