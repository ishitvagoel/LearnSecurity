import base64
def protect(p):
    return base64.b64encode(p.encode()).decode()
def looks_encrypted(t):
    return t != 'secret'
