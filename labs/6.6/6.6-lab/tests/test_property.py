def test_invite_token_is_single_use(impl):
    assert impl.accept("t1") is True
    assert impl.accept("t1") is False


def test_distinct_tokens_are_independent(impl):
    assert impl.accept("t1") is True
    assert impl.accept("t2") is True
    assert impl.accept("t2") is False
