def isolation_enforced(headers):
    # Vulnerable: Report-Only is treated as enforcement.
    return (
        "Content-Security-Policy-Report-Only" in headers
        or "Content-Security-Policy" in headers
    )
