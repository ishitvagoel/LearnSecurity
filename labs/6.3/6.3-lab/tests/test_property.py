def test_foreign_origin_post_is_denied(impl):
    assert (
        impl.allow_share(
            "https://evil.example",
            "https://app.securecollab.test",
            token=None,
        )
        is False
    )


def test_same_origin_without_token_is_denied(impl):
    assert (
        impl.allow_share(
            "https://app.securecollab.test",
            "https://app.securecollab.test",
            token=None,
        )
        is False
    )


def test_same_origin_with_token_is_allowed(impl):
    assert (
        impl.allow_share(
            "https://app.securecollab.test",
            "https://app.securecollab.test",
            token="lab-csrf",
        )
        is True
    )


def test_missing_cookie_is_denied(impl):
    assert (
        impl.allow_share(
            "https://app.securecollab.test",
            "https://app.securecollab.test",
            token="lab-csrf",
            session_cookie=False,
        )
        is False
    )
