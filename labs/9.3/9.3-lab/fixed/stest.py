def is_security_test(t):
    return bool(t.get('forbidden_outcome'))
