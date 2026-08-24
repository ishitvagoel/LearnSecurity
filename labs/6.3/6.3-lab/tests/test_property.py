def test_foreign_origin_post_is_denied(impl):
    assert impl.allow_share('https://evil.example', 'https://app.securecollab.test', token=None) is False
