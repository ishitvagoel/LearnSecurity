def test_is_admin_cannot_be_patched(impl):
    u={'display_name':'a','is_admin':False}
    out=impl.apply(u, {'is_admin':True})
    assert out['is_admin'] is False
