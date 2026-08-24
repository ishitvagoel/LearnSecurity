def covered(req_id, tests):
    return any(t.get('req') == req_id and t.get('asserts_isolation') for t in tests)
