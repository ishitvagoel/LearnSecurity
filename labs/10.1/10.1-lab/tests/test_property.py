def test_merge_requires_threat_model_id(impl):
    assert impl.merge_ok({}) is False


def test_pr_with_threat_model_may_merge(impl):
    assert impl.merge_ok({"threat_model": "TM-12"}) is True
