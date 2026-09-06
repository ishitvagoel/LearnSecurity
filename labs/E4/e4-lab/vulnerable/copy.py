def copy_into(bufsize, src, declared_len):
    # Vulnerable: trusts declared_len over the destination size.
    return src[: declared_len + 8]
