def test_does_not_invoke_shell(impl):
    try:
        cmd = impl.argv_for_list('notes')
    except ValueError:
        assert impl.uses_shell('notes') is False
        return
    assert cmd[:2] != ['sh', '-c']
    assert impl.uses_shell('notes') is False
