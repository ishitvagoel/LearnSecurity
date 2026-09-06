def boot_ok(env, debug):
    # Vulnerable: production with debug=True still boots.
    return True
