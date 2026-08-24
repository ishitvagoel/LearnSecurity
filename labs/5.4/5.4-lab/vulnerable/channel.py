def channel_is_https(headers, server_scheme):
    return headers.get('X-Forwarded-Proto') == 'https' or server_scheme == 'https'
