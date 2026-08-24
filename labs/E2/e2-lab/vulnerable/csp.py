def isolation_enforced(headers):
    return 'Content-Security-Policy-Report-Only' in headers or 'Content-Security-Policy' in headers
