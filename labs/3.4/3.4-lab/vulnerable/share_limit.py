_n = 0

def reset():
    global _n
    _n = 0

def add_share() -> int:
    global _n
    _n += 1
    return _n
