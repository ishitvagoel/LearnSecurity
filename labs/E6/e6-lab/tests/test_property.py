def test_exception_needs_owner_review_and_wcag(impl):
    assert impl.accept_exception({"owner": "", "review_by": None}) is False


def test_complete_exception_may_be_accepted(impl):
    assert (
        impl.accept_exception(
            {"owner": "alice", "review_by": "2026-12-01", "wcag_checked": True}
        )
        is True
    )
