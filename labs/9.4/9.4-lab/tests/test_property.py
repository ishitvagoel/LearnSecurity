def test_unmapped_high_blocks_ship(impl):
    assert impl.ship_ok([{'id': 'F1', 'sev': 'HIGH'}], {}) is False
