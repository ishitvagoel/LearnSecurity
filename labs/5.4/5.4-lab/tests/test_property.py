def test_server_https_counts(impl) -> None:
    assert impl.channel_is_https({}, "https") is True


def test_plain_http_is_not_https(impl) -> None:
    assert impl.channel_is_https({}, "http") is False


def test_client_forwarded_proto_is_not_tls(impl) -> None:
    assert impl.channel_is_https({"X-Forwarded-Proto": "https"}, "http") is False
