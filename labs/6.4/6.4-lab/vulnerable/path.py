from pathlib import Path
ROOT=Path('/tmp/sc-lab')
def resolve(name):
    return str(ROOT / name)
