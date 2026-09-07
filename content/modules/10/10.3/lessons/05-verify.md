# A broken admission must fail the check

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

Running Kubernetes does not deny `cluster-admin`. A green CIS scan is a score. `pod_ok("cluster-admin")` has to be false, and `"app"` may run. On the broken files cluster-admin still runs. On the repaired files it does not. Do not apply manifests to a live cluster.

## Picture: a broken admission must fail the check

A passing-test tally can still hide that `pod_ok("cluster-admin")` still returns true.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: cluster-admin runs]
  X["repaired files --impl fixed"] --> P[Must pass: cluster-admin denied]
```

If both pass, you are not looking at cluster-admin.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | `app` → may run (may pass on both) |
| Wrong input | cluster-admin → cannot run; broken files must fail |
| Abuse | Unknown roles still deny (fail closed) |
| Not claimed | A live managed cluster; a CIS score; an assurance gate; that `"app"` is least privilege |

The test `test_cluster_admin_pod_is_denied` is there so always-true `pod_ok` still fails.

A pod using `"app"` may pass on both sides. You still have to deny cluster-admin. If the broken files do not fail `test_cluster_admin_pod_is_denied`, the lab is miswired — fix the wiring, not the assertion.

```text
python3 -m pytest labs/10.3/10.3-lab/tests --impl vulnerable
python3 -m pytest labs/10.3/10.3-lab/tests --impl fixed
```

A `namespace:` line in a chart is not `pod_ok("cluster-admin")`. This practice never opens a live cluster.

## What the tests do not prove

- A restricted pod profile on the real spec
- Network-policy egress
- Instance metadata blocked
- Helm chart supply chain
- Documented cluster-API retry (extra, advanced)
- This page does not finish a cluster check-in

## Practice

Call `pod_ok("cluster-admin")`. A `namespace:` line in a chart is inventory.

## Use it somewhere new

A namespace that exists is inventory, not `pod_ok("cluster-admin")`. Do not use a live kube-apiserver.

## What this page is not doing

A live cluster screenshot is not `cluster-admin` denied. Do not log kubeconfig. Answer keys are not on this site. This page does not mark you as finished.
