# Lab 10.3

Authorized: this directory only. No live targets.

An app pod must not run as cluster-admin. Cloud IAM is complete mediation of the cluster API, not 'we use Kubernetes.'

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: app pod with role cluster-admin.
