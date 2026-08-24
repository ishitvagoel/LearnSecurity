def test_exec_sql_tool_is_denied(impl):
    assert impl.run_tool('exec_sql', {}) is None
