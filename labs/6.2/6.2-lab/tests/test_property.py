def test_angle_brackets_are_encoded(impl):
    out = impl.render("<img src=x>")
    assert "<img" not in out
    assert "&lt;" in out


def test_honest_title_survives(impl):
    out = impl.render("Weekly notes")
    assert "Weekly notes" in out
