ALLOWED_ROLES = frozenset({"app"})


def pod_ok(role):
    # Structural stand-in: only named namespaced roles may run.
    # This is not a Kubernetes admission controller or RBAC engine.
    return role in ALLOWED_ROLES
