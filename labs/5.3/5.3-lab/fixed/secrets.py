def auth(presented: str, current=None) -> bool:
    return bool(current) and presented == current
