def test_copy_does_not_exceed_buffer(impl):
    out = impl.copy_into(4, b'abcdefgh', 4)
    assert len(out) <= 4
