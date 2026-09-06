def test_does_not_invoke_shell(impl):
    try:
        cmd = impl.argv_for_list("notes")
    except ValueError:
        assert impl.uses_shell("notes") is False
        return
    assert cmd[:2] != ["sh", "-c"]
    assert impl.uses_shell("notes") is False


def test_argv_is_program_then_name(impl):
    cmd = impl.argv_for_list("notes")
    assert cmd[0] != "sh"
    assert cmd[-1] == "notes"
    assert impl.uses_shell("notes") is False
