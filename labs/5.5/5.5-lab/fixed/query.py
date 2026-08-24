def fetch_sql(tenant, note_id):
    return ("SELECT body FROM notes WHERE tenant=%s AND id=%s", (tenant, note_id))
def is_bound(q):
    return isinstance(q, tuple) and len(q[1])==2
