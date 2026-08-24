NOTES={'alice':'secret'}
ANALYTICS={'alice':'secret'}
def reset():
    NOTES.clear(); NOTES['alice']='secret'
    ANALYTICS.clear(); ANALYTICS['alice']='secret'
def delete_account(user):
    NOTES.pop(user, None)
def body_retained(user):
    return ANALYTICS.get(user)
