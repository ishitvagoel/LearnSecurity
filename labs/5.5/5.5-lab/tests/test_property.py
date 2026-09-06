def test_query_is_bound_not_concatenated(impl):
    q = impl.fetch_sql("tA", "n1' OR '1'='1")
    if isinstance(q, str):
        assert False, "concatenated SQL is not complete mediation of the interpreter"
    assert impl.is_bound(q)
    sql, params = q
    assert "%s" in sql
    assert params == ("tA", "n1' OR '1'='1")


def test_honest_note_id_is_still_bound(impl):
    q = impl.fetch_sql("tA", "n1")
    assert not isinstance(q, str)
    assert impl.is_bound(q)
