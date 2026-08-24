def test_client_forwarded_proto_is_not_tls(impl):
    assert impl.channel_is_https({'X-Forwarded-Proto':'https'}, 'http') is False
