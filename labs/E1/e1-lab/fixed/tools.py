ALLOWED = frozenset({"search_notes"})


def run_tool(name, args):
    # Structural stand-in: only allowlisted tools run. Not a production agent runtime.
    if name not in ALLOWED:
        return None
    return f"ran {name}"
