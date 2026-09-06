ALLOWED_ROLES = frozenset({"app"})


def pod_ok(role):
    # Vulnerable: any requested role, including cluster-admin, is treated as runnable.
    return True
