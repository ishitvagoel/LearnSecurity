# 10.3-LO-07 — Transfer: clinic app SA is cluster-admin

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** NIST SP 800-190 as stack vocabulary. Kubernetes PSS as pod hardening. ASVS `v5.0.0-13.2.1`. `v5.0.0-13.2.6` Level 3 **advanced**.

## Change the workplace; keep namespace from meaning isolation

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `pod_ok("cluster-admin")` must be false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic: app SA is cluster-admin. Also name serverless IAM `*`.

**Product sketch:** EHR-lite “the API namespace is private so ClusterRole is fine,” plus “we attached a NetworkPolicy and a CIS Kubernetes scan.”

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (compromised container / malicious chart — not a live clinic cluster attack);
2. trust assumptions (allowlisted namespaced role is TCB; namespace/NetworkPolicy/PSS/CIS are not);
3. forbidden outcome (`pod_ok("cluster-admin")` true, not “HIPAA”);
4. a test idea on a **local** fixture only (no live kube-apiserver);
5. residual (break-glass E6, IMDS hop, `v5.0.0-13.2.6` Level 3);
6. WCAG if admission is human-read (say cluster-admin refused).

## Mental model: private namespace vs ClusterRole

```mermaid
flowchart LR
  Ns[private namespace] --> Belief[isolated]
  Sa[cluster-admin SA] --> Reality[control plane]
```

If the namespace is “private” while `pod_ok` is always true, the cell is gone. NetworkPolicy, PSS `restricted`, and a CIS scan do not put `"app"` in `ALLOWED_ROLES`. Serverless IAM `*` is the same god-mode grain on a different object — name it, do not attack a live cloud account here. NIST SP 800-190 names five layers; it does not make EKS secure by default. `v5.0.0-13.2.6` is Level 3 advanced: documented cluster-API retry, not this pytest.

The clinic rewrite still has to keep the SecureCollab fork: cluster-admin denied, app may run. Adding a namespace without an allowlist leaves `pod_ok("cluster-admin")` true. The local pytest analogue is `test_cluster_admin_pod_is_denied` — on a fixture, not a live cluster.

## What graders reject

| Reject | Why |
|---|---|
| “we have NetworkPolicy” | Egress, not RBAC |
| Live cluster / cloud takeover tutorial | Lab policy |
| “PSS restricted so 1.2 is done” | Pod spec ≠ API authorization |
| “CIS scan green” | Benchmark, not the predicate |
| “Gate 10 complete” | Forbidden stamp |

## Practice

One page. No keys. `labs/10.3/10.3-lab` is the only running system you may break. Do not apply YAML to a live cluster.

## Non-goals

Live-cluster attacks. Real cloud-account takeover. Claiming Gate 10 or M4 from this page.
