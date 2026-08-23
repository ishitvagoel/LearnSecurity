_n = 0
MAX = 5

def reset():
    global _n
    _n = 0

def add_share() -> int:
    global _n
    if _n >= MAX:
        return _n
    _n += 1
    return _n
