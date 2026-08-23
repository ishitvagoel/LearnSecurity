ALLOWED={'display_name'}
def apply(user, body):
    for k,v in body.items():
        if k in ALLOWED:
            user[k]=v
    return user
