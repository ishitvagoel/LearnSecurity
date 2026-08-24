from pathlib import Path
ROOT=Path('/tmp/sc-lab').resolve()
def resolve(name):
    p = (ROOT / name).resolve()
    if ROOT not in p.parents and p != ROOT:
        raise ValueError('escape')
    return str(p)
