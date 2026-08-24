def test_localhost_lab_is_in_scope(scope) -> None:
    assert scope.target_is_authorized("http://127.0.0.1:8000/notes") is True


def test_public_host_is_out_of_scope(scope) -> None:
    assert scope.target_is_authorized("https://example.com/") is False, (
        "course work is not authorization to attack the public internet"
    )
