def test_client_integrity_claim_is_not_authorization(impl):
    assert impl.allow_export({'integrity': 'ok'}, 'fail') is False
