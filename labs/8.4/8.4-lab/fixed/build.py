def api_allowed(build_type, attest):
    return build_type == 'release' and attest == 'ok'
