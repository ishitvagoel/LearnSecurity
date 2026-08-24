def test_hardcoded_default_does_not_auth(impl):
    assert impl.auth('sk-lab-hardcoded', current='rotated-now') is False
