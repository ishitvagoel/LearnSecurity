SESSION={'user':'alice'}
def reset():
    SESSION['user']='alice'
def open_link(query):
    if 'as' in query:
        SESSION['user']=query['as']
def current_user():
    return SESSION['user']
