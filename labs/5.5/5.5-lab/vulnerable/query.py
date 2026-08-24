def fetch_sql(tenant, note_id):
    return f"SELECT body FROM notes WHERE tenant='{tenant}' AND id='{note_id}'"
def is_bound(sql):
    return '%s' in sql or '?' in sql
