def covered(req_id, tests):
    return any(t.get('req') == req_id for t in tests)
