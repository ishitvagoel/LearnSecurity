CHARGES=[]
def reset():
    CHARGES.clear()
def capture(key):
    CHARGES.append(key)
    return True
def charge_count():
    return len(CHARGES)
