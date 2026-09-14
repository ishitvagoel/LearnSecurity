def test_alice_can_read_her_company_note(app) -> None:
    assert app.read_note("alice", "n1").status == 200


def test_bob_cannot_read_alices_note(app) -> None:
    response = app.read_note("bob", "n1")
    assert response.status == 403
    assert response.body == {"error": "denied"}


def test_client_company_label_cannot_change_the_decision(app) -> None:
    response = app.read_note("bob", "n1", client_company="company-a")
    assert response.status == 403
