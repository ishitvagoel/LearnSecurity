def test_exception_needs_owner_review_and_wcag(impl):
    assert impl.accept_exception({'owner': '', 'review_by': None}) is False
