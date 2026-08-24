ALLOWED={'search_notes'}
def run_tool(name, args):
    if name not in ALLOWED:
        return None
    return f'ran {name}'
