def test_eval_on_user_input_is_rejected(impl):
    assert impl.review_ok("x = eval(user)") is False


def test_honest_diff_without_eval_may_pass(impl):
    assert impl.review_ok("x = int(user)") is True
