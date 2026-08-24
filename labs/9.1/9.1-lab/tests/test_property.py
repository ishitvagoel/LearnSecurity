def test_status_only_row_is_not_coverage(impl):
    tests = [{'req': 'AUTHZ-1', 'asserts_isolation': False}]
    assert impl.covered('AUTHZ-1', tests) is False
