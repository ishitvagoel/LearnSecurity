# Lab 10.3 — a namespace is not cluster-admin

**Module:** `10.3`
**Authorized scope:** this directory only. Local course fixture. No live clusters, cloud accounts, or public Kubernetes APIs.
**Invariant:** `pod_ok("cluster-admin")` is false. A namespaced `app` role may run.
**Root cause class:** god-mode for convenience (always-true admission)
**Non-goals:** NetworkPolicy as RBAC; EKS/GKE product defaults as 1.2; claiming Gate 10 or M4.

The allowlist of role names is a **teaching stand-in** for a namespaced RoleBinding plus Pod Security Admission `restricted`. It is not a kube-apiserver.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/10.3/10.3-lab`, then run `git restore --source=HEAD -- labs/10.3/10.3-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`pod_ok` always returns true. Forbidden outcome: app pod granted `cluster-admin`.

## Structural fix

Require `role in ALLOWED_ROLES` (`{"app"}`). Denying only the string `cluster-admin` would still be a denylist, not least privilege.

## Verify

```
python3 -m pytest labs/10.3/10.3-lab/tests --impl vulnerable
python3 -m pytest labs/10.3/10.3-lab/tests --impl fixed
```

The first command must fail on `cluster-admin`. The second must pass. Honest `app` may pass on both.

## Operate

Signal: `cluster_admin_denied`. Do not log kubeconfig contents or cloud tokens. Do not claim Gate 10 or M4.

## Transfer

Clinic: app service account is `cluster-admin`. Prompt only. Serverless IAM `*` is the same grain.
