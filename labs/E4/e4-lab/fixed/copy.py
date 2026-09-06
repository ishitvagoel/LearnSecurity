def copy_into(bufsize, src, declared_len):
    # Structural stand-in: bound the copy by destination, declared length, and src.
    # This is not a C exploit and not ASAN.
    n = min(bufsize, declared_len, len(src))
    return src[:n]
