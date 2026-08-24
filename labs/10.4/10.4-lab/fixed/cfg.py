def boot_ok(env, debug):
    return not (env == 'prod' and debug)
