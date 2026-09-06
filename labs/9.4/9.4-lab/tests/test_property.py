def test_unmapped_high_blocks_ship(impl):
    assert impl.ship_ok([{"id": "F1", "sev": "HIGH"}], {}) is False


def test_mapped_high_may_ship(impl):
    assert impl.ship_ok([{"id": "F1", "sev": "HIGH"}], {"F1": "AUTHZ-1"}) is True
