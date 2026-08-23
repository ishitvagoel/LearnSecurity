def test_eval_on_user_input_is_rejected(impl):
    assert impl.review_ok('x = eval(user)') is False
