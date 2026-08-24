SEEN=set(); CHARGES=[]
def reset():
    SEEN.clear(); CHARGES.clear()
def capture(key):
    if key in SEEN:
        return False
    SEEN.add(key)
    CHARGES.append(key)
    return True
def charge_count():
    return len(CHARGES)
