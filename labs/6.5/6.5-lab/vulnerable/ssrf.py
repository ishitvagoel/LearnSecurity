from urllib.parse import urlparse
def allowed(url):
    return urlparse(url).scheme in {'http','https'}
