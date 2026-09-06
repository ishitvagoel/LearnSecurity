from pathlib import Path

LAB_ROOT = "/tmp/sc-lab"


def test_dotdot_does_not_escape_root(impl):
    try:
        p = impl.resolve("../outside")
    except ValueError:
        return
    resolved = str(Path(p).resolve())
    assert resolved == LAB_ROOT or resolved.startswith(LAB_ROOT + "/")


def test_honest_relative_stays_under_root(impl):
    p = impl.resolve("notes/a.txt")
    resolved = str(Path(p).resolve())
    assert resolved.startswith(LAB_ROOT)
