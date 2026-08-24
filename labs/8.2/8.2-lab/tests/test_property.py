def test_cached_note_is_not_plaintext_on_disk(impl):
    impl.save_note('secret')
    assert impl.plaintext_on_disk() is False
