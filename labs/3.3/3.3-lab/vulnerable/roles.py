"""Vulnerable roles: any role can read any tenant; runtime user is superuser."""


def runtime_connection_role() -> str:
    return "postgres"


def can_select(role: str, tenant: str, note_tenant: str) -> bool:
    return True
