NOTES={'n1': {'tenant': 'A', 'body': 'secret'}}
GRANTS={('n1', 'B')}
def reset():
    GRANTS.clear(); GRANTS.add(('n1', 'B'))
def revoke(nid, tenant):
    GRANTS.discard((nid, tenant))
def read(nid, tenant):
    n = NOTES[nid]
    if tenant == n['tenant'] or (nid, tenant) in GRANTS:
        return n['body']
    return None
