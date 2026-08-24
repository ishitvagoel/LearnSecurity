_used=set()
def reset():
    _used.clear()
def accept(token):
    if token in _used:
        return False
    _used.add(token)
    return True
