"""Fixed roles: runtime app may SELECT only the bound tenant."""

RUNTIME_SELECT_ROLES = frozenset({"app"})


def runtime_connection_role() -> str:
    return "app"


def can_select(role: str, tenant: str, note_tenant: str) -> bool:
    if role not in RUNTIME_SELECT_ROLES:
        return False
    return tenant == note_tenant
