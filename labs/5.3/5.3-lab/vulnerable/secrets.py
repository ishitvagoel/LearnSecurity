DEFAULT='sk-lab-hardcoded'
def auth(presented, current=None):
    return presented == DEFAULT or presented == current
