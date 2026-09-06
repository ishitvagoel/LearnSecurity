def test_current_secret_authenticates(impl) -> None:
    assert impl.auth("rotated-now", current="rotated-now") is True


def test_hardcoded_default_does_not_auth(impl) -> None:
    assert impl.auth("sk-lab-hardcoded", current="rotated-now") is False


def test_missing_current_denies(impl) -> None:
    assert impl.auth("rotated-now", current=None) is False
