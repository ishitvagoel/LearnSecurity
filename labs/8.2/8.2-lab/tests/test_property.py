def test_cached_note_is_not_plaintext_on_disk(impl):
    impl.save_note("secret")
    assert impl.plaintext_on_disk() is False


def test_other_body_is_not_reported_as_plaintext_secret(impl):
    impl.save_note("other")
    assert impl.plaintext_on_disk() is False
