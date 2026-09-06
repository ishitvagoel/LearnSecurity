def boot_ok(env, debug):
    # Structural: production cannot boot while debug is on.
    # Other flags (feature, migration) are residual — see lessons.
    if env == "prod" and debug:
        return False
    return True
