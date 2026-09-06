NOTES = {"n1": {"tenant": "A", "body": "secret"}}
GRANTS = {("n1", "B")}


def reset():
    GRANTS.clear()
    GRANTS.add(("n1", "B"))


def revoke(nid, tenant):
    # Vulnerable: revoke is a no-op. The grant is never consulted on read.
    pass


def read(nid, tenant):
    return NOTES[nid]["body"]
