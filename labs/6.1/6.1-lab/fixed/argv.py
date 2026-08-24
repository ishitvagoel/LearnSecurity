def argv_for_list(name):
    if any(c in name for c in ' 	;|&$`'):
        raise ValueError('rejected')
    return ['ls', name]
def uses_shell(name):
    return False
