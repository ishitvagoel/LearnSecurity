ALWAYS = ["cross-tenant-read", "hostile-browser", "stolen-worker"]

def threats_from_scan(scanner_green: bool) -> list[str]:
    return list(ALWAYS)
