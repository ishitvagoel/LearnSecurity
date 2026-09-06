def close_incident(inc):
    # Vulnerable: any ticket close is treated as done.
    return True
