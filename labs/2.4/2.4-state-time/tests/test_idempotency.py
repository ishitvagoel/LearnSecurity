def test_single_share(share) -> None:
    share.share_note("n1", idempotency_key="k1")
    assert share.share_count() == 1


def test_retry_does_not_duplicate_side_effect(share) -> None:
    share.share_note("n1", idempotency_key="k1")
    share.share_note("n1", idempotency_key="k1")
    assert share.share_count() == 1, "timeouts/retries must not fail-open into a second share"
