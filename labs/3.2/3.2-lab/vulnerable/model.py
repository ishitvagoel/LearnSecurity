def threats_from_scan(scanner_green: bool) -> list[str]:
    return [] if scanner_green else ["generic"]
