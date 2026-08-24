def allow_share(origin, expected, token=None, session_cookie=True):
    if not session_cookie:
        return False
    return origin == expected and token == 'lab-csrf'
