def auth(presented, current=None):
    return bool(current) and presented == current
