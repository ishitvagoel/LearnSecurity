def test_exec_sql_tool_is_denied(impl):
    assert impl.run_tool("exec_sql", {}) is None


def test_allowlisted_search_notes_may_run(impl):
    assert impl.run_tool("search_notes", {}) == "ran search_notes"
