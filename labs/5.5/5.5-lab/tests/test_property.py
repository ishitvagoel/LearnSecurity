def test_query_is_bound_not_concatenated(impl):
    q = impl.fetch_sql('tA', "n1' OR '1'='1")
    if isinstance(q, str):
        assert False, 'concatenated SQL is not complete mediation of the interpreter'
    assert impl.is_bound(q)
