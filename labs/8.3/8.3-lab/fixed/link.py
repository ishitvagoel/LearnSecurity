SESSION={'user':'alice'}
def reset():
    SESSION['user']='alice'
def open_link(query):
    return None
def current_user():
    return SESSION['user']
