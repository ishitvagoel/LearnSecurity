def test_link_local_metadata_is_denied(impl):
    assert impl.allowed('http://169.254.169.254/latest') is False
def test_lab_host_https_ok(impl):
    assert impl.allowed('https://lab.securecollab.test/og') is True
