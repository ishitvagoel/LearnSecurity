def test_merge_requires_threat_model_id(impl):
    assert impl.merge_ok({}) is False
