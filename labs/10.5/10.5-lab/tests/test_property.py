def test_cannot_close_without_recovery(impl):
    assert impl.close_incident({'recovery': 'todo', 'logs': 'ok'}) is False
