def test_same_tenant_cache_hit(cache) -> None:
    cache.cache_put("/notes/n1", "tA", "tenant-A-note")
    assert cache.cache_get("/notes/n1", "tA") == "tenant-A-note"


def test_other_tenant_does_not_receive_cached_body(cache) -> None:
    cache.cache_put("/notes/n1", "tA", "tenant-A-note")
    got = cache.cache_get("/notes/n1", "tB")
    assert got != "tenant-A-note", "cache key must include bound tenant; TLS does not imply this"
    assert got is None
