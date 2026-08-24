def protect(p):
    # stand-in for an AEAD; teaching flag only
    return 'aesgcm:' + str(len(p))
def looks_encrypted(t):
    return t.startswith('aesgcm:')
