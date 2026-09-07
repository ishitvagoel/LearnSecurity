# Practice: always-true pod_ok

**Kind:** mechanism-lab
**Loop step:** 3 Break

## Try it

The practice is not a cluster you attack. It is a tiny Python `pod_ok` that returns true for every role. The failure is already in the function: it never looks at the role. You are here to see that the check treats that always-true admission as a **failed rule**, not as a paperwork nit.

The rule under test:

> An app pod must not run as cluster-admin. If `pod_ok("cluster-admin")` returns true, admission has failed as a security control.

## Where you may practice

Only `labs/10.3/10.3-lab` is in scope. The practice is an in-process `pod_ok(role)`. The roles are synthetic strings `cluster-admin` / `app`. Do **not** apply ClusterRoleBindings to a real cluster, cloud account, or shared lab Kubernetes as the exercise.

Do not paste this exercise onto a public cluster, employer account, or live hospital Kubernetes "to see what happens."

What is supposed to stop this: `pod_ok` is supposed to allow **only namespaced app roles**. Managed-cluster defaults, a restricted pod profile, a network policy, and FastAPI itself are not enough.

Who can take the cluster in this story: a compromised container or a malicious Helm chart. That stands in for "the API namespace is private so ClusterRole is fine," a CIS Kubernetes scan treated as the who-is-allowed check, or a network policy treated as RBAC.

## Picture: admission always says yes

```mermaid
flowchart TD
  Any[any role] --> True[pod_ok true]
```

The broken files take that path on purpose. You do not need a kube-apiserver. You must not bind a live cluster. The true return for `"cluster-admin"` *is* the leak.

The database god-role lesson already said one shared admin is a blast-radius rule. This check is **the same idea at cluster grain**.

## What to look at — cause, not a dump

Read `vulnerable/iam.py`. It returns true for every role. Tests:

- `test_cluster_admin_pod_is_denied`
- `test_namespaced_app_role_may_run` — `"app"` may pass on both

You do not need a new role string. The failure of `test_cluster_admin_pod_is_denied` *is* the evidence.

Do not open the repaired files yet. Diagnose the cause first.

| What you see | What kind of failure | Not the lesson |
|---|---|---|
| `return True` for every role | Always-true admission; god-mode for convenience | "The namespace is private" |
| `"cluster-admin"` still runs | What must not happen is allowed | A CIS score |
| No look at `"app"` membership | The gate accepted a god role | A network policy |

## Why it happens vs what it costs

| Slice | Practice |
|---|---|
| The rule | `pod_ok("cluster-admin")` is false |
| Why it happens | Always-true admission; god-mode for convenience |
| What has to be true first | `pod_ok` true for every role |
| Trigger | Compromised container or malicious chart |
| What it costs | One app bug becomes control-plane takeover |
| How you stop it later | Allow-list namespaced roles; unknown roles deny |
| How you notice later | `cluster_admin_denied`; never kubeconfig |
| How you recover later | Delete the binding; rotate cluster credentials |
| Out of scope | A CIS score; a live managed cluster; claiming an assurance gate |

A managed cluster will still accept a ClusterRoleBinding. A restricted pod profile hardens the *pod spec*. FastAPI will still run as whatever SA the chart mounts. The notes app's API will still take the cluster if admission is always true. The app's promise this week is: **this** practice, `cluster-admin` is deny.

## Practice

From the repository root, in a throwaway environment:

```text
python3 -m pytest labs/10.3/10.3-lab/tests --impl vulnerable
```

Run from `labs/10.3/10.3-lab` if a collection at the repo root picks up `site/`. Record `test_cluster_admin_pod_is_denied`. Do not probe public hosts. A setup error is not proof the rule holds.

## Use it somewhere new

Clinic app SA is cluster-admin: predict without leaving this directory. Do not apply manifests to a live cluster.

## What this page is not doing

No live-cluster, cloud-account, or public Kubernetes API instructions. This page does not mark you as finished. Do not fetch instance metadata as an exercise.
