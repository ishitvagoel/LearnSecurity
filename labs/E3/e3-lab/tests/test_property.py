def test_duplicate_capture_does_not_double_charge(impl):
    impl.capture("k1")
    impl.capture("k1")
    assert impl.charge_count() == 1


def test_first_capture_may_charge(impl):
    assert impl.capture("k1") is True
    assert impl.charge_count() == 1
