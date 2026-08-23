def resolve(role, field):
    if field=='secret_internal':
        return role=='service'
    return True
