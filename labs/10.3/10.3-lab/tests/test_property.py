def test_cluster_admin_pod_is_denied(impl):
    assert impl.pod_ok("cluster-admin") is False


def test_namespaced_app_role_may_run(impl):
    assert impl.pod_ok("app") is True
