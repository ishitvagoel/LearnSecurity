def test_cluster_admin_pod_is_denied(impl):
    assert impl.pod_ok('cluster-admin') is False
