def allow_export(client_claims, server_attest):
    return client_claims.get('integrity') == 'ok'
