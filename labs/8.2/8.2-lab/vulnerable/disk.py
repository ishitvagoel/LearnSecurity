DISK={}
def reset():
    DISK.clear()
def save_note(body):
    DISK['note']=body
def plaintext_on_disk():
    return DISK.get('note')=='secret'
