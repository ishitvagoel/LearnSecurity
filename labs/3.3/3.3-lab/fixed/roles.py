def can_select(role: str, tenant: str, note_tenant: str) -> bool:
    if role != "app":
        return False
    return tenant == note_tenant
