def test_dotdot_does_not_escape_root(impl):
    try:
        p = impl.resolve('../etc/passwd')
    except ValueError:
        return
    assert '/etc/passwd' not in p.replace('\\','/')
    assert p.startswith('/tmp/sc-lab')
