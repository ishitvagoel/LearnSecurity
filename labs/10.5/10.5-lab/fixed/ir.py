def close_incident(inc):
    logs = inc.get('logs', '')
    return inc.get('recovery') == 'done' and 'note_body' not in logs
