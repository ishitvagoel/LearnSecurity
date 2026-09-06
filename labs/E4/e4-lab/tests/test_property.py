def test_copy_does_not_exceed_buffer(impl):
    out = impl.copy_into(4, b"abcdefgh", 4)
    assert len(out) <= 4


def test_short_copy_may_fit(impl):
    out = impl.copy_into(4, b"ab", 2)
    assert out == b"ab"
