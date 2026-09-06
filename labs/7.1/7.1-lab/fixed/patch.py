ALLOWED = {"display_name"}


def apply(user, body):
    for key, value in body.items():
        if key in ALLOWED:
            user[key] = value
    return user
