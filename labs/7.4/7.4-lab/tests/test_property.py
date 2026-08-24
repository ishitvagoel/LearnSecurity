def test_user_session_is_not_worker_identity(impl):
    assert impl.exporter({'user_session':'alice','service':None}) is None
