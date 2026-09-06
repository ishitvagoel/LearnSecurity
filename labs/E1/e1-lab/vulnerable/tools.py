ALLOWED = frozenset({"search_notes"})


def run_tool(name, args):
    # Vulnerable: any model-proposed tool name runs.
    return f"ran {name}"
