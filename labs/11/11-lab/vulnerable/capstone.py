NOTES={'n1': {'tenant': 'A', 'body': 'secret'}}
GRANTS={('n1', 'B')}
def reset():
    GRANTS.clear(); GRANTS.add(('n1', 'B'))
def revoke(nid, tenant):
    pass
def read(nid, tenant):
    n = NOTES[nid]
    return n['body']
