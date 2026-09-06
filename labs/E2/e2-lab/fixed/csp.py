def isolation_enforced(headers):
    # Structural: only an enforcing CSP header counts. Report-Only is a signal.
    return "Content-Security-Policy" in headers
