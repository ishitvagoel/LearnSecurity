def ship_ok(findings, mappings):
    return all(f['id'] in mappings for f in findings if f.get('sev') == 'HIGH')
