CHARGES = []


def reset():
    CHARGES.clear()


def capture(key):
    # Vulnerable: every call appends a charge.
    CHARGES.append(key)
    return True


def charge_count():
    return len(CHARGES)
