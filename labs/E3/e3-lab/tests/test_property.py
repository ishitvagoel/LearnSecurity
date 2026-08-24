def test_duplicate_capture_does_not_double_charge(impl):
    impl.capture('k1')
    impl.capture('k1')
    assert impl.charge_count() == 1
