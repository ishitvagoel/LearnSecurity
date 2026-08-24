def allow_export(client_claims, server_attest):
    return server_attest == 'play_integrity_pass'
