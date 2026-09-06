def close_incident(inc):
    # Structural: recovery evidence is required, and logs are not a body store.
    logs = inc.get("logs", "")
    return inc.get("recovery") == "done" and "note_body" not in logs
