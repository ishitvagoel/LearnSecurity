def test_share_cap_is_enforced(impl) -> None:
    last = 0
    for _ in range(8):
        last = impl.add_share()
    assert last <= 5
