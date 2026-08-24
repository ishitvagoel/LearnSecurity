def copy_into(bufsize, src, declared_len):
    n = min(bufsize, declared_len, len(src))
    return src[:n]
