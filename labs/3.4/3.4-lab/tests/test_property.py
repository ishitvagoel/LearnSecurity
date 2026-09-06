def test_share_cap_is_enforced(impl) -> None:
    last = 0
    for _ in range(8):
        last = impl.add_share()
    assert last <= 5


def test_five_shares_are_allowed(impl) -> None:
    last = 0
    for _ in range(5):
        last = impl.add_share()
    assert last == 5


def test_sixth_does_not_increment(impl) -> None:
    for _ in range(5):
        impl.add_share()
    assert impl.add_share() == 5
